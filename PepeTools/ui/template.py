import bpy
from bpy.types import Panel
from bpy.types import PropertyGroup
from bpy.types import Operator
from bpy.props import PointerProperty

from .. import settings
from PepeTools.util.debug_msg import outputDebugString


class PETOOLS_PT_TemplateProps(PropertyGroup):
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
    pass


# Define the panel class
class PETOOLS_PT_Template(Panel):
    # Override : 3Dビューに表示する
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    # Override :
    bl_category = settings.TAB_NAME
    bl_label = "Template Panel"
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout
        # props = context.scene.templateProps

        layout.label(text="Template Panel")
        layout.operator("pepe.btn_kind", text="Push!!", icon="MESH_CUBE")


class MyButton1(Operator):
    bl_idname = "pepe.btn_kind"
    bl_label = "MyButton1"

    def execute(self, context):
        outputDebugString("Call")
        return {'FINISHED'}


# List of classes to register
classes = [
    PETOOLS_PT_TemplateProps,
    PETOOLS_PT_Template,
    MyButton1,
]


def register():
    outputDebugString("Call")
    # Register the panel
    for cls in classes:
        bpy.utils.register_class(cls)

    # Register the property group
    bpy.types.Scene.templateProps = PointerProperty(type=PETOOLS_PT_TemplateProps)


# Unregister the panel
def unregister():
    outputDebugString("Call")
    # Unregister the panel
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # Unregister the property group
    del bpy.types.Scene.templateProps


# Entry point for testing the add-on
if __name__ == "__main__":
    register()
