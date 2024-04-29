# -*- coding: utf-8 -*-
# ファイル名: __init__.py
# 説明: PepeToolsアドオンのエントリーポイント
# 作成者: Pepe Weekend (kaff.brand.pepe@gmail.com)
# バージョン: 1.0.0
# ライセンス: MIT License (https://opensource.org/licenses/MIT)
# 著作権: (c) 2024 Pepe Weekend
#
# 更新履歴:
#   - 2024-04-30: 初版作成
try:
    import bpy
except ImportError:
    print(__doc__)
    import sys
    sys.exit()

from . import settings
from PepeTools.util.debug_msg import outputDebugString
from PepeTools.settings import logger

ADDON_FOLDER_NAME = "PepeTools"
ADDON_FOLDER_NAME_UI = "ui"
ADDON_FOLDER_NAME_OPRATOR = "op"
ADDON_FOLDER_NAME_UTILITY = "util"

# -----------------------------------------------------------------------------------------------
# プロパティクラスの登録
# -----------------------------------------------------------------------------------------------
bl_info = {
    "name": "Pepe Tools",
    "author": "Pepe",
    "version": (0, 0, 1),
    "blender": (4, 1, 0),
    "location": "View3D",
    "description": "Tools for Pepe",
    "warning": "開発中",
    "support": "COMMUNITY",
    "wiki_url": "https://github.com/PepeWeekend/PepeTools",
    "tracker_url": "",
    "category": "Object",
}

# -----------------------------------------------------------------------------------------------
# add-on有効化時メッセージ
# -----------------------------------------------------------------------------------------------
start_msg_lists = [
    "# ====================================================",
    "# Start Activation Pepe Tools",
    f"#  - author    : {bl_info['author']}",
    f"#  - version   : {bl_info['version']}",
    "# ====================================================",
]
for msg in start_msg_lists:
    logger.output(msg, logger.MsgType.System)

# -----------------------------------------------------------------------------------------------
# モジュールのリロード
# -----------------------------------------------------------------------------------------------
if 'bpy' in locals():
    from importlib import reload
    import sys
    for k, v in list(sys.modules.items()):
        if k.startswith(ADDON_FOLDER_NAME):
            if v.__name__ != __name__:
                outputDebugString(f"reload module : {v}", 'System')
                reload(v)
            else:
                outputDebugString(f"not reload module : {v}", 'System')


# --------------------------------REGISTER-------------------------------------------------------
# __init__.py内クラス登録
classes = [
    # PepeToolKet_AddonPreferences
]

# Add-on有効化情報
# setting.pyのENABLE_FUNCTION_LISTで有効化する機能を設定
register_list = settings.ENABLE_FUNCTION_LIST


def register():
    '''登録処理
    '''
    outputDebugString("PepeTools Regist Start!!", 'System')
    for cls in classes:
        bpy.utils.register_class(cls)

    for lst in register_list:
        if lst.register is not None:
            lst.register()
        else:
            outputDebugString(f"{lst} has no register method", 'Error')

    outputDebugString("PepeTools Registed Finish!!", 'System')


def unregister():
    '''登録解除処理
    '''
    outputDebugString("PepeTools UnRegist Start!!", 'System')
    for lst in register_list:
        if lst.unregister is not None:
            lst.unregister()
        else:
            outputDebugString(f"{lst} has no unregister method", 'Error')

    for cls in classes:
        bpy.utils.unregister_class(cls)

    outputDebugString("PepeTools UnRegisted Finish!!", 'System')


if __name__ == "__main__":
    '''Add-on登録時処理
    '''
    register()
