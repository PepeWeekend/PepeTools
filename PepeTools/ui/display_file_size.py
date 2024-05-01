# import stand alone modules
import os
import sys
import bpy
from bpy_types import PropertyGroup
from bpy.props import FloatProperty
from bpy.props import FloatVectorProperty
import blf


from .. import settings
from PepeTools.util.debug_msg import call_log_decorator
from PepeTools.util.get_classes import get_classes
from PepeTools.util.debug_msg import logger

font_info = {
    "font_id": 0,
    "handler": None,
}

counter = 0


# -------------------------------PROPERTY---------------------------------------

class PETOOLS_PT_show_file_size_props(PropertyGroup):
    # bpy.props
    # Bool        : BoolProperty(default=True, name="Check Box")
    # String      : StringProperty(default="hoge", name="String")
    # Int         : IntProperty(default=44, name="Int",min=0,max=100)
    # Float       : FloatProperty(default=3.14, name="Float",min=0)
    # FloatVector : FloatVectorProperty(default=(0.1,0.2,0.3), name="name")
    # Enum        : EnumProperty(default="Scene",name="Enum", items= [
    #                               ("Selected","Selected","Selected","RESTRICT_SELECT_OFF",0),
    #                               ("Scene","Scene","Scene","SCENE_DATA",1),
    #                               ("All_Data","All Data","All Data","FILE",2),
    #                           ])
    # Pointer     : PointerProperty(name="Target Object",type=bpy.types.Object)
    file_limit: FloatProperty(default=3.14, min=0)
    font_color: FloatVectorProperty(default=(1.0, 0.0, 0.0), min=0.0, max=1.0, subtype='COLOR_GAMMA')


# リージョン情報の取得


def get_region(context, area_type, region_type):
    """
    指定されたエリアとリージョンの情報を取得

    Parameters
    ----------
    context : bpy.types.Context
        コンテキスト
    area_type : str
        エリアのタイプ
    region_type : str
        リージョンのタイプ

    Returns
    -------
    bpy.types.Region
        リージョン情報
    """
    region = None
    area = None

    # 指定されたエリアの情報を取得する
    for a in context.screen.areas:
        if a.type == area_type:
            area = a
            break
    else:
        return None
    # 指定されたリージョンの情報を取得する
    for r in area.regions:
        if r.type == region_type:
            region = r
            break

    return region


# ----------------------------------OT------------------------------------------

class PETOOLS_OT_show_file_size(bpy.types.Operator):
    bl_idname = "object.sample35_show_datetime"
    bl_label = "日時を表示"
    bl_description = "日時を表示します"

    __handle = None

    @classmethod
    def is_running(self):
        # 描画中はTrue
        return True if self.__handle else False

    @classmethod
    def __handle_add(self, context):
        if not self.is_running():
            # 描画関数の登録
            self.__handle = bpy.types.SpaceView3D.draw_handler_add(
                self.__draw, (context, ), 'WINDOW', 'POST_PIXEL'
            )

    @classmethod
    def __handle_remove(self, context):
        if self.is_running():
            # 描画関数の登録を解除
            bpy.types.SpaceView3D.draw_handler_remove(
                self.__handle, 'WINDOW'
            )
            self.__handle = None

    @classmethod
    def __draw(self, context):
        props = context.scene.show_file_size_props
        global counter
        font_id = 0
        counter = counter + 1

        #
        region = get_region(context, 'VIEW_3D', 'WINDOW')

        # ファイルサイズ取得
        filepath = bpy.data.filepath
        file_size = 0.0
        if filepath:
            file_size = os.path.getsize(filepath)
            file_size = file_size / 1024 / 1024

        # 表示色判定
        if file_size < props.file_limit:
            blf.color(font_id, 1.0, 1.0, 1.0, 1.0)
        else:
            blf.color(font_id, props.font_color[0], props.font_color[1], props.font_color[2], 1.0)

        blf.position(font_id, 65, region.height - 250, 0)
        blf.size(font_id, 11.0)
        blf.shadow(font_id, 3, 1.0, 1.0, 1.0, 1.0)
        blf.draw(font_id, f"ファイルサイズ : {file_size:.2} MB")

    def invoke(self, context, event):
        op_cls = PETOOLS_OT_show_file_size

        if context.area.type == 'VIEW_3D':
            if not op_cls.is_running():
                self.__handle_add(context)
            else:
                self.__handle_remove(context)

            # エリアを再描画
            if context.area:
                context.area.tag_redraw()
            return {'FINISHED'}
        else:
            return {'CANCELLED'}


# ----------------------------------PT------------------------------------------
class PETOOLS_PT_show_file_size(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    bl_category = settings.TAB_NAME
    bl_label = "ファイルサイズ表示"
    bl_context = "objectmode"

    def draw(self, context):
        props = context.scene.show_file_size_props
        op_cls = PETOOLS_OT_show_file_size

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="表示", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="非表示", icon="PAUSE")

        layout.separator()
        layout.label(text="警告表示設定:")
        layout.prop(props, "file_limit", text="警告上限(MB)")
        layout.prop(props, "font_color", text="表示色")

        layout.label(text="表示設定:")
        layout.label(text="表示位置:")


# --------------------------------REGISTER--------------------------------------
# List of classes to register
classes = list(get_classes(sys.modules[__name__], __name__))


@call_log_decorator
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        logger.output(f"Register Class : {cls}", logger.MsgType.Info)

    # Register the property group
    # bpy.types.Scene.templateProps = PointerProperty(type=PETOOLS_PT_TemplateProps)
    bpy.types.Scene.show_file_size_props = bpy.props.PointerProperty(type=PETOOLS_PT_show_file_size_props)


@call_log_decorator
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Unregister the property group
    # del bpy.types.Scene.templateProps
    del bpy.types.Scene.show_file_size_props


if __name__ == '__main__':
    # register()
    pass
