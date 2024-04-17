# import stand alone modules
import blf
import bpy

import sys
from .. import settings
from PepeTools.util.debug_msg import OutputDebugString as ODS
from PepeTools.util.debug_msg import call_log_decorator
from PepeTools.util.get_classes import get_classes

font_info = {
    "font_id": 0,
    "handler": None,
}

counter = 0

# リージョン情報の取得


def get_region(context, area_type, region_type):
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


class SAMPLE35_OT_show_file_size(bpy.types.Operator):
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
        global counter
        font_id = 0
        counter = counter + 1

        region = get_region(context, 'VIEW_3D', 'WINDOW')

        blf.position(font_id, 200, region.height - 580, 0)
        # blf.position(font_id, 200, 580, 0)
        blf.size(font_id, 16.0)
        blf.draw(font_id, f"Hello World : {counter}")

    def invoke(self, context, event):
        op_cls = SAMPLE35_OT_show_file_size

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


class PETOOLS_PT_show_file_size(bpy.types.Panel):

    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    bl_category = settings.TAB_NAME
    bl_label = "ファイルサイズ表示"
    bl_context = "objectmode"

    def draw(self, context):
        op_cls = SAMPLE35_OT_show_file_size

        layout = self.layout
        # [開始] / [停止] ボタンを追加
        if not op_cls.is_running():
            layout.operator(op_cls.bl_idname, text="開始", icon="PLAY")
        else:
            layout.operator(op_cls.bl_idname, text="終了", icon="PAUSE")


def init():
    """init function - runs once"""

    font_info["font_id"] = 0

    # set the font drawing routine to run every frame
    font_info["handler"] = bpy.types.SpaceView3D.draw_handler_add(
        draw_callback_px, (None, None), 'WINDOW', 'POST_PIXEL')


def draw_callback_px(self, context):
    """Draw on the viewports"""
    # region = get_region(context, 'VIEW_3D', 'WINDOW')

    # BLF drawing routine
    font_id = font_info["font_id"]
    # blf.position(font_id, 200, region.height - 580, 0)
    blf.position(font_id, 200, 580, 0)
    blf.size(font_id, 16.0)
    blf.draw(font_id, "Hello World")


classes = list(get_classes(sys.modules[__name__], __name__))


@call_log_decorator
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        ODS().output(f"Register Class : {cls}", ODS.MsgType.Info)

    # Register the property group
    # bpy.types.Scene.templateProps = PointerProperty(type=PETOOLS_PT_TemplateProps)


@call_log_decorator
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Unregister the property group
    # del bpy.types.Scene.templateProps


if __name__ == '__main__':
    register()
