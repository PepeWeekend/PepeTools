# -*- coding: utf-8 -*-
"""PepeToolsアドオンの設定ファイル

このファイルはPepeToolsアドオンの設定ファイルです。
PepeToolsはPepe Weekendによって開発されたBlenderのツールセットです。
"""
TAB_NAME = "PepeTools"

from PepeTools.ui import wait_set_button
from PepeTools.ui import display_model_info
# from PepeTools.ui import template
# from PepeTools.ui import restart
# from PepeTools.ui import display_file_size

# List of functions to enable.
ENABLE_FUNCTION_LIST = [
    wait_set_button,        # Set the weight.
    display_model_info      # Display the model information.
    # template,               # Display the template panel.
    # restart,                # Restart the addon.
    # display_file_size,      # Display the file size.
]
