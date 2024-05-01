# -*- coding: utf-8 -*-
"""PepeToolsアドオンのモデル情報表示モジュール

概要: モデル情報を表示するためのモジュール
"""

try:
    import bpy
    from bpy.types import Panel
    from bpy.types import Operator
    from bpy_types import PropertyGroup

except ImportError:
    print(__doc__)
    raise

import os
import datetime

from .. import settings
from PepeTools.util.debug_msg import logger
from PepeTools.util.debug_msg import call_log_decorator


# -------------------------------PROPERTY---------------------------------------


class PETOOLS_PT_display_model_info_props(PropertyGroup):
    """モデル情報を表示するためのプロパティグループ

    """
    pass


# ----------------------------------PT------------------------------------------
class PETOOLS_PT_display_model_info(Panel):
    """ モデル情報を表示するためのパネル

    """

    # Override : 3Dビューに表示する
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    # Override :
    bl_category = settings.TAB_NAME
    bl_label = "ファイル内モデル情報表示/保存"
    bl_options = {'DEFAULT_CLOSED'}

    # ---------------------------------コレクション内オブジェクト情報--------------------------------------

    class collection:
        """コレクション内オブジェクト情報

        """

        def __init__(self):
            self.total_vertex_count: int = 0      # 頂点数
            self.total_material_count: int = 0    # マテリアル数
            self.total_triangle_count: int = 0    # 三角形数
            self.total_sarface_count: int = 0     # 面数
            self.mesh_names: list[str] = []       # メッシュ名
            self.material_names: list[str] = []   # マテリアル名
            self.mesh_infos: list[dict] = []

        def clear(self):
            """初期化

            """
            self.total_vertex_count = 0
            self.total_material_count = 0
            self.total_triangle_count = 0
            self.total_sarface_count = 0
            self.mesh_names.clear()
            self.material_names.clear()
            self.mesh_infos.clear()

    collection = collection()

    # ---------------------------------ファイル内のオブジェクト情報----------------------------------------
    class project:
        """ファイル内のオブジェクト情報

        """

        def __init__(self):
            self.total_material_count: int = 0    # マテリアル数
            self.material_names: list[str] = []   # マテリアル名
            self.file_size: int = 0               # ファイルサイズ

        def clear(self):
            """class内保持情報初期化

            """
            self.total_material_count = 0
            self.material_names.clear()
            self.file_size = 0

    project = project()

    class error_messaga:
        """エラーメッセージ

        Args:
            message (str) : エラーメッセージ
            param (list[str]) : パラメータ
            format (str) : フォーマット

        """

        def __init__(self, message: str = "unknown error message", param: list[str] = None, format: str = ""):
            self.message = message
            self.param = param
            if len(format) <= 0:
                self.format = f"{message} : {param}"
            else:
                self.format = format

    class SaveFileInfoButton(Operator):
        """ファイル保存ボタン

        Args:
            Operator (bpy.types.Operator) : Blender Operator
        """
        bl_idname = "pepe.btn_kind2"
        bl_label = "MyButton2"

        def execute(self, context) -> dict[str]:
            """ボタン押下時実行処理

            Args:
                context (bpy.context) : コンテキスト

            Returns:
                dict[str] : 処理終了状態

                {'FINISHED'} : 正常終了

            """
            op_cls = PETOOLS_PT_display_model_info

            op_cls.collection.clear()
            op_cls.project.clear()

            # 編集ファイル情報更新
            op_cls._update_file_info(context)

            # ファイル内情報の整合性確認
            err_msgs = op_cls._check_file_different()

            # ファイル保存
            op_cls._save_file(context, err_msgs)

            return {'FINISHED'}

    def save_handler(scene):
        """ファイル保存ハンドラ

        Args:
            scene (bpy.types.Scene) : シーン情報

        """
        logger.output("File Save Process Start......", logger.MsgType.Info)

        try:
            op_cls = PETOOLS_PT_display_model_info

            op_cls.collection.clear()
            op_cls.project.clear()

            try:
                # 編集ファイル情報更新
                op_cls._update_file_info(scene)
            except Exception as e:
                logger().output(f"File Save Process Error [_update_file_info] : {e}", logger.MsgType.Error)
                return

            # ファイル内情報の整合性確認
            err_msgs = op_cls._check_file_different()

            # ファイル保存
            try:
                op_cls._save_file(scene, err_msgs)
            except Exception as e:
                logger.output(f"File Save Process Error [_save_file] : {e}", logger.MsgType.Error)
                return

            logger.output("File Save Process Success", logger.MsgType.Info)

        except Exception as e:
            logger.output(f"File Save Process Error : {e}", logger.MsgType.Error)

    def draw(self, context):
        """パネル描画処理

        Args:
            context (bpy.context) : コンテキスト

        """
        layout = self.layout

        self.collection.clear()
        self.project.clear()

        # 編集ファイル情報更新
        self._update_file_info(context)

        # ファイル内情報の整合性確認
        err_msgs = self._check_file_different()

        # パネル描画
        self._draw_panel(context, layout, err_msgs)

    @classmethod
    def _update_file_info(self, context):
        """ファイル情報更新

        Args:
            context (bpy.context) : コンテキスト

        """
        # 存在オブジェクトの情報
        for obj in bpy.context.scene.objects:
            if obj is not None and obj.type == 'MESH':
                # 三角形数を計算
                obj.data.calc_loop_triangles()
                triangles_count = len(obj.data.loop_triangles)
                self.collection.total_vertex_count += len(obj.data.vertices)
                self.collection.total_triangle_count += triangles_count
                self.collection.total_sarface_count += len(obj.data.polygons)

                # メッシュ名を取得
                self.collection.mesh_names.append(obj.name)

                # メッシュ情報を取得
                self.collection.mesh_infos.append({
                    "name": obj.name,
                    "data": obj.data
                })

                for mat in obj.data.materials:
                    if mat is not None:
                        self.collection.material_names.append(mat.name)

                # Remove duplicates from the material names list
                self.collection.material_names = list(set(self.collection.material_names))

        # ファイル内のマテリアル定義数を取得
        for mat in bpy.data.materials:
            self.project.total_material_count += 1
            self.project.material_names.append(mat.name)

        # Get the file size
        file_size = 0
        try:
            file_size = os.path.getsize(bpy.data.filepath) / 1000 / 1000  # Byte -> MB
        except Exception:
            pass

        self.project.file_size_mb = file_size

    def _draw_panel(self, context, layout, err_msgs):
        """パネルを描画する

        Args:
            layout (bpy.types.UILayout) : レイアウト
            err_msgs (list[str]) : エラーメッセージ

        """
        # --------------------------------------------------------------------------------------
        # Infomation
        # --------------------------------------------------------------------------------------
        # ファイル保存ボタン
        layout.operator("pepe.btn_kind2", text="ファイル保存", icon="FILE_TICK")

        # ファイル内基本情報
        info_lines = []
        info_lines.append(f" - 総頂点数     : {self.collection.total_vertex_count}")
        info_lines.append(f" - 総面数       : {self.collection.total_sarface_count}")
        info_lines.append(f" - 三角形面     : {self.collection.total_triangle_count}")
        info_lines.append(f" - マテリアル数 : {self.project.total_material_count}")
        for line in info_lines:
            layout.label(text=line)

        # --------------------------------------------------------------------------------------
        # Warning
        # --------------------------------------------------------------------------------------
        # 警告情報
        if err_msgs is not None:
            layout.separator()
            box = layout.box()
            box.label(text="警告", icon='ERROR')
            for msg in err_msgs:
                box.label(text=msg.format)

    @classmethod
    def _check_file_different(self) -> list[str]:
        """ファイル内の情報が異なるか確認する

        Returns:
            disp_err_msg : list[str]

        """
        disp_err_msg: list[self.error_messaga] = []

        # 未保存のファイルを捜査している場合
        if self.project.file_size_mb == 0:
            ERROR_MSG_NON_FILE = "編集中のファイルが未保存状態です"
            disp_err_msg.append(self.error_messaga(ERROR_MSG_NON_FILE))

        # ファイル内のマテリアル定義数が異なる場合
        ERROR_MSG_MATERIALS_DIFFERENT = "ファイル内に余分なマテリアルが含まれています"
        if len(self.collection.material_names) != len(self.project.material_names):
            diff_materials = set(self.collection.material_names) ^ set(self.project.material_names)
            for diff in diff_materials:
                disp_err_msg.append(self.error_messaga(ERROR_MSG_MATERIALS_DIFFERENT, diff))

        return disp_err_msg

    @classmethod
    def _save_file(self, context, disp_err_msg: list[str] = None):
        """ファイルを保存する

        Args:
            context (bpy.context) : コンテキスト
            disp_err_msg (list[str]) : エラーメッセージ

        """
        # --------------------------------------------------------------------------------------
        # Infomation File output
        # --------------------------------------------------------------------------------------
        # Get the Blender project file path
        project_file_path = bpy.data.filepath
        project_file_path = project_file_path[:project_file_path.rfind("\\")]
        project_file_name = bpy.path.basename(bpy.data.filepath)
        output_file_path = f"{project_file_path}//{project_file_name}_info.txt"

        # Get the current date and time
        current_datetime = datetime.datetime.now()

        # Convert the datetime object to a string
        current_datetime_str = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

        # Write the current date and time to a file
        lines = []
        lines.append(f"Current Date and Time: {current_datetime_str}")
        lines.append("==============================================================================")
        lines.append(f"Save Path : {project_file_path}")
        lines.append(f"File Name : {project_file_name}")
        lines.append(f"File Size : {self.project.file_size_mb:.2f} MB")
        lines.append("------------------------------------------------------------------------------")
        lines.append("Basic File Infomation :")
        lines.append(f" - 総頂点数     : {self.collection.total_vertex_count}")
        lines.append(f" - 総面数       : {self.collection.total_sarface_count}")
        lines.append(f" - 三角形面     : {self.collection.total_triangle_count}")
        lines.append(f" - マテリアル数 : {self.project.total_material_count}")
        lines.append("")

        lines.append("Waring File Info :")
        if disp_err_msg is not None:
            for msg in disp_err_msg:
                lines.append(f" - {msg.format}")
        else:
            lines.append(" - None")
        lines.append("")

        lines.append("Advance File Infomation :")
        lines.append(" + File into Mesh Names :")
        for mesh_info in self.collection.mesh_infos:
            lines.append(f"   - {mesh_info['name']} : ")
            lines.append(f"     頂点 : {len(mesh_info['data'].vertices)}"
                         f", 辺 : {len(mesh_info['data'].edges)}"
                         f", 面 : {len(mesh_info['data'].polygons)}"
                         f", マテリアル : {len(mesh_info['data'].materials)}"
                         f" {list(mat.name for mat in mesh_info['data'].materials)}")

        lines.append(" + File into Material Names :")
        for material_name in self.project.material_names:
            lines.append(f"   - {material_name}")

        lines.append("")
        lines.append("")

        # --------------------------------------------------------------------------------------
        # Write the project file path to a file
        import tempfile
        import shutil
        with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp_file:
            # with open(output_tmp_file_path, "w+") as tmp_file:
            if not os.path.exists(output_file_path):
                with open(output_file_path, 'w') as file:
                    pass

            with open(output_file_path, 'r') as file:
                shutil.copyfileobj(file, tmp_file)

            tmp_file.seek(0)
            tmp_file.write('\n'.join(lines))

            with open(output_file_path, 'r') as f:
                shutil.copyfileobj(f, tmp_file)

        shutil.move(tmp_file.name, output_file_path)

        logger.output(f"Infomation File Save : {output_file_path}", logger.MsgType.Info)

        # --------------------------------------------------------------------------------------
        # Infomation
        # --------------------------------------------------------------------------------------
        '''
        for obj in bpy.context.selected_objects:
            layout.label(text=f"Object Name: {obj.name}")
            layout.label(text=f"Object Type: {obj.type}")
            layout.label(text=f"Object Location: {obj.location}")
            layout.label(text=f"Object Rotation: {obj.rotation_euler}")
            layout.label(text=f"Object Scale: {obj.scale}")
            layout.label(text=f"Object Dimensions: {obj.dimensions}")
            layout.label(text=f"Object Vertices: {len(obj.data.vertices)}")
            layout.label(text=f"Object Edges: {len(obj.data.edges)}")
            layout.label(text=f"Object Faces: {len(obj.data.polygons)}")
            layout.label(text=f"Object Materials: {len(obj.data.materials)}")
            layout.label(text=f"Object UV Maps: {len(obj.data.uv_layers)}")
            layout.label(text=f"Object Vertex Colors: {len(obj.data.vertex_colors)}")
            # layout.label(text=f"Object Shape Keys: {len(obj.data.shape_keys.key_blocks)}")
            layout.label(text=f"Object Armature: {obj.find_armature()}")
            layout.label(text=f"Object Parent: {obj.parent}")
            layout.label(text=f"Object Children: {obj.children}")
            layout.label(text=f"Object Modifiers: {len(obj.modifiers)}")
            layout.label(text=f"Object Constraints: {len(obj.constraints)}")
            # layout.label(text=f"Object Drivers: {len(obj.animation_data.drivers)}")
            # layout.label(text=f"Object Actions: {len(obj.animation_data.action.fcurves)}")
            layout.label(text=f"Object Particles: {len(obj.particle_systems)}")
            layout.label(text=f"Object Physics: {obj.rigid_body}")
            layout.label(text=f"Object Display: {obj.display_type}")
            layout.label(text=f"Object Visibility: {obj.hide_viewport}")
        '''


# --------------------------------REGISTER--------------------------------------
# List of classes to register
# classes = list(get_classes(sys.modules[__name__], __name__))
classes = [
    PETOOLS_PT_display_model_info,
    PETOOLS_PT_display_model_info.SaveFileInfoButton,
    PETOOLS_PT_display_model_info_props
]


@ call_log_decorator
def register():
    """クラス登録
    """
    for cls in classes:
        logger.output(f"Register Class : {cls}", logger.MsgType.Info)
        bpy.utils.register_class(cls)

    # Register the property group
    bpy.types.Scene.display_model_imfo_props = bpy.props.PointerProperty(type=PETOOLS_PT_display_model_info_props)

    # ファイルセーブハンドラ登録
    logger.output("File Save Handler append to List", logger.MsgType.Info)
    bpy.app.handlers.save_post.append(PETOOLS_PT_display_model_info.save_handler)


@ call_log_decorator
def unregister():
    """クラス解除
    """
    for cls in classes:
        bpy.utils.unregister_class(cls)

    # プロパティグループ削除
    del bpy.types.Scene.display_model_imfo_props

    # ファイルセーブハンドラ削除
    try:
        bpy.app.handlers.save_post.remove(PETOOLS_PT_display_model_info.save_handler)
    except Exception as e:
        logger.output(f"File Save Handler is not find in List : {e}", logger.MsgType.Error)


if __name__ == "__main__":
    # register()
    pass
