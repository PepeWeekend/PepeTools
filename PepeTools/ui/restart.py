#!/usr/bin/python
# -*- coding: utf-8 -*-
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
    # Override : 3Dビューに表示する
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    # Override :
    bl_category = settings.TAB_NAME
    bl_label = "Restart Blender"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        # props = context.scene.templateProps

        layout.label(text="まだ再起動しません(終了しますん)")
        layout.operator("pepe.reboot_blender", text="Restart", icon="MESH_CUBE")

        self.draw_restart_button(context)

    # 要素毎にまとめて関数化するのがよさそうです
    def draw_restart_button(self, context):
        layout = self.layout
        layout.operator("pepe.reboot_blender", text="Restart Blender")

    # ボタンを押した時の処理を記述する
    class Operator(bpy.types.Operator):
        bl_idname = "pepe.reboot_blender"
        bl_label = "Restart Blender"
        # bl_description = "Restart Blender application"
        # bl_options = {'REGISTER'}

        def execute(self, context):
            ODS().output("Call", ODS.MsgType.Error)
            self.reboot_blender(context)
            return {'FINISHED'}

        def reboot_blender(self, context):
            # bpy.ops.wm.quit_blender()
            pass


# ----------------------------------CLS-----------------------------------------
# List of classes to register
classes = list(get_classes(sys.modules[__name__], __name__))


@call_log_decorator
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register the property group
    # bpy.types.Scene.templateProps = PointerProperty(type=PETOOLS_PT_TemplateProps)


@call_log_decorator
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Unregister the property group
    # del bpy.types.Scene.templateProps


if __name__ == "__main__":
    register()
