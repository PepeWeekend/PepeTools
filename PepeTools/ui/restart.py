try:
    import bpy
    from bpy.types import Panel
except ImportError:
    print(__doc__)
    raise

import sys
from .. import settings
from PepeTools.util.debug_msg import OutputDebugString as ODS
from PepeTools.util.debug_msg import call_log_decorator
from PepeTools.util.get_classes import get_classes

# ----------------------------------PT------------------------------------------


class PETOOLS_PT_restart(Panel):
    '''
    Blender再起動パネル
    '''
    # Override : 3Dビューに表示する
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    # Override :
    bl_category = settings.TAB_NAME
    bl_label = "Restart Blender"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        '''
        描画処理

        Parameters
        ----------
        context : bpy.types.Context
            コンテキスト

        Returns
        -------
        None
        '''
        layout = self.layout
        # props = context.scene.templateProps

        layout.label(text="まだ再起動しません(終了しますん)")
        layout.operator("pepe.reboot_blender", text="Restart", icon="MESH_CUBE")

        self.draw_restart_button(context)

    # 要素毎にまとめて関数化するのがよさそうです
    def draw_restart_button(self, context):
        '''
        再起動ボタン描画

        Parameters
        ----------
        context : bpy.types.Context
            コンテキスト

        Returns
        -------
        None
        '''
        layout = self.layout
        layout.operator("pepe.reboot_blender", text="Restart Blender")

    # ボタンを押した時の処理を記述する
    class Operator(bpy.types.Operator):
        '''
        Blender再起動クラス

        Parameters
        ----------
        bpy : bpy.types.Operator
            Blender Operator

        Returns
        -------
        None
        '''
        bl_idname = "pepe.reboot_blender"
        bl_label = "Restart Blender"
        # bl_description = "Restart Blender application"
        # bl_options = {'REGISTER'}

        def execute(self, context):
            '''
            実行処理

            Parameters
            ----------
            context : bpy.types.Context
                コンテキスト

            Returns
            -------
            {'FINISHED'}
            '''
            ODS().output("Call", ODS.MsgType.Error)
            self.reboot_blender(context)
            return {'FINISHED'}

        def reboot_blender(self, context):
            '''
            Blender再起動

            Parameters
            ----------
            context : bpy.types.Context
                コンテキスト

            Returns
            -------
            None
            '''
            # bpy.ops.wm.quit_blender()
            pass


# --------------------------------REGISTER--------------------------------------
# List of classes to register
classes = list(get_classes(sys.modules[__name__], __name__))


@call_log_decorator
def register():
    """
    クラス登録
    """
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register the property group
    # bpy.types.Scene.templateProps = PointerProperty(type=PETOOLS_PT_TemplateProps)


@call_log_decorator
def unregister():
    """
    クラス登録を解除
    """
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # プロパティグループを登録解除します
    # del bpy.types.Scene.templateProps


if __name__ == "__main__":
    register()
