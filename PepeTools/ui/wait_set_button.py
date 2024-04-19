import sys
import bpy
from .. import settings
from PepeTools.util.debug_msg import OutputDebugString as ODS
from PepeTools.util.debug_msg import call_log_decorator
from PepeTools.util.get_classes import get_classes


class PETOOLS_PT_wait_set_button(bpy.types.Panel):
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    bl_category = settings.TAB_NAME
    bl_label = "ウェイト設定ボタン"
    bl_context = "weightpaint"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        now_wait = bpy.context.scene.tool_settings.unified_paint_settings.weight
        layout.label(text=f"現在ウェイト値 {now_wait:.3f}")

        box = layout.box()
        col = box.column()
        sp = col.split(align=True, factor=0.50)
        sp.operator(self.Operator_0000.bl_idname, text=f"{self.Operator_0000.wait:.3f}")
        sp.operator(self.Operator_1000.bl_idname, text=f"{self.Operator_1000.wait:.3f}")

        sp = col.split(align=True, factor=0.33)
        sp.operator(self.Operator_0250.bl_idname, text=f"{self.Operator_0250.wait:.3f}")
        sp.operator(self.Operator_0500.bl_idname, text=f"{self.Operator_0500.wait:.3f}")
        sp.operator(self.Operator_0750.bl_idname, text=f"{self.Operator_0750.wait:.3f}")

        sp = col.split(align=True, factor=0.25)
        sp.operator(self.Operator_0125.bl_idname, text=f"{self.Operator_0125.wait:.3f}")
        sp.operator(self.Operator_0385.bl_idname, text=f"{self.Operator_0385.wait:.3f}")
        sp.operator(self.Operator_0625.bl_idname, text=f"{self.Operator_0625.wait:.3f}")
        sp.operator(self.Operator_0875.bl_idname, text=f"{self.Operator_0875.wait:.3f}")

    class Operator_0000(bpy.types.Operator):
        wait = 0.000
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0125(bpy.types.Operator):
        wait = 0.125
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0250(bpy.types.Operator):
        wait = 0.250
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0385(bpy.types.Operator):
        wait = 0.385
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0500(bpy.types.Operator):
        wait = 0.500
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0625(bpy.types.Operator):
        wait = 0.625
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0750(bpy.types.Operator):
        wait = 0.750
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_0875(bpy.types.Operator):
        wait = 0.875
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}

    class Operator_1000(bpy.types.Operator):
        wait = 1.000
        bl_idname = "pepe.btn_wait_" + str(int(wait * 1000))
        bl_label = bl_idname

        def execute(self, context):
            bpy.context.scene.tool_settings.unified_paint_settings.weight = self.wait
            return {'FINISHED'}


# --------------------------------REGISTER--------------------------------------
# List of classes to register
classes = list(get_classes(sys.modules[__name__], __name__))


@call_log_decorator
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
        ODS().output(f"Register Class : {cls}", ODS.MsgType.Info)


@call_log_decorator
def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == '__main__':
    register()
