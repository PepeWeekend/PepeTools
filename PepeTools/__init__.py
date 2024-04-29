# -*- coding: utf-8 -*-
"""
PepeToolsアドオンのエントリーポイント

@file __init__.py
@brief PepeToolsアドオンのエントリーポイント
@details このファイルはPepeToolsアドオンのエントリーポイントです。
PepeToolsはPepe Weekendによって開発されたBlenderのツールセットです。

@author Pepe Weekend
@version 1.0.0
@license GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.html)
@date 2024-04-30 初版作成
"""
try:
    import bpy
except ImportError:
    print(__doc__)
    import sys
    sys.exit()

from PepeTools.settings import ENABLE_FUNCTION_LIST
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
    from sys import modules
    for k, v in list(modules.items()):
        if k.startswith(ADDON_FOLDER_NAME):
            if v.__name__ != __name__:
                logger.output(f"reload module : {v}", logger.MsgType.System)
                reload(v)
            else:
                logger.output(f"not reload module : {v}", logger.MsgType.System)


# --------------------------------REGISTER-------------------------------------------------------
# __init__.py内クラス登録
classes = [
    # PepeToolKet_AddonPreferences
]

# Add-on有効化情報
# setting.pyのENABLE_FUNCTION_LISTで有効化する機能を設定
register_list = ENABLE_FUNCTION_LIST


def register():
    '''!
    @brief アドオン登録
    '''
    logger.output("PepeTools Regist Start!!", logger.MsgType.System)

    # クラス登録
    for cls in classes:
        bpy.utils.register_class(cls)

    # 機能登録
    for lst in register_list:
        if lst.register is not None:
            lst.register()
        else:
            logger.output(f"{lst} has no register method", logger.MsgType.Error)

    logger.output("PepeTools Registed Finish!!", logger.MsgType.System)


def unregister():
    '''!
    @brief アドオン解除
    '''
    logger.output("PepeTools UnRegist Start!!", logger.MsgType.System)

    # 機能解除
    for lst in register_list:
        if lst.unregister is not None:
            lst.unregister()
        else:
            logger.output(f"{lst} has no unregister method", logger.MsgType.Error)

    # クラス解除
    for cls in classes:
        bpy.utils.unregister_class(cls)

    logger.output("PepeTools UnRegisted Finish!!", logger.MsgType.System)


if __name__ == "__main__":
    register()
