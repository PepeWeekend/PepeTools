# -*- coding: utf-8 -*-
"""
PepeToolsアドオンの設定ファイル

@file settings.py
@brief PepeToolsアドオンの設定ファイル
@details このファイルはPepeToolsアドオンの設定ファイルです。
PepeToolsはPepe Weekendによって開発されたBlenderのツールセットです。

@author Pepe Weekend
@version 1.0.0
@license GNU General Public License v3.0 (https://www.gnu.org/licenses/gpl-3.0.html)
@date 2024-04-30 初版作成
"""
TAB_NAME = "PepeTools"

from PepeTools.util.debug_msg import OutputDebugString as dbg

# from PepeTools.ui import template
# from PepeTools.ui import restart
# from PepeTools.ui import display_file_size
from PepeTools.ui import wait_set_button
from PepeTools.ui import display_model_info

"""
List of functions to enable.
"""
ENABLE_FUNCTION_LIST = [
    # template,               # Display the template panel.
    # restart,                # Restart the addon.
    # display_file_size,      # Display the file size.
    wait_set_button,        # Set the weight.
    display_model_info      # Display the model information.
]

# Debug message outputer
logger = dbg()
