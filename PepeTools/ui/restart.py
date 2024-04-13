import bpy
from bpy.types import Panel

from .. import settings
from PepeTools.util.debug_msg import outputDebugString


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

        layout.label(text="まだ再起動しません(終了します)")
        layout.operator("pepe.reboot_blender", text="Restart", icon="MESH_CUBE")

        self.draw_restart_button(context)

    def draw_restart_button(self, context):
        layout = self.layout
        layout.operator("pepe.reboot_blender", text="Restart Blender")

    # class RestartBlenderOperator(bpy.types.Operator):
    class Operator(bpy.types.Operator):
        bl_idname = "pepe.reboot_blender"
        bl_label = "Restart Blender"
        # bl_description = "Restart Blender application"
        # bl_options = {'REGISTER'}

        def execute(self, context):
            outputDebugString("Call", 'Error')
            reboot_blender(self, context)
            return {'FINISHED'}


def reboot_blender(self, context):
    # bpy.ops.wm.quit_blender()
    pass


# List of classes to register
classes = [
    PETOOLS_PT_restart,
    PETOOLS_PT_restart.Operator,
]


def register():
    outputDebugString("Call")
    # Register the panel
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register the property group
    # bpy.types.Scene.templateProps = PointerProperty(type=PETOOLS_PT_TemplateProps)


# Unregister the panel
def unregister():
    outputDebugString("Call")
    # Unregister the panel
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Unregister the property group
    # del bpy.types.Scene.templateProps


if __name__ == "__main__":
    register()
