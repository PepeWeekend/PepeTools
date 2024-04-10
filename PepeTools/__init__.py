#!/usr/bin/python
# -*- coding: utf-8 -*-
import bpy
# from . import settings
from PepeTools.ui import template
from PepeTools.util.debug_msg import outputDebugString

ADDON_FOLDER_NAME = "PepeTools"
ADDON_FOLDER_NAME_UI = "ui"
ADDON_FOLDER_NAME_OPRATOR = "op"
ADDON_FOLDER_NAME_UTILITY = "util"

bl_info = {
    "name": "Pepe Tools",
    "author": "Pepe",
    "version": (0, 0, 1),
    "blender": (4, 1, 0),
    "location": "View3D",
    "description": "Tools for Pepe",
    "warning": "開発中",
    "support": "COMMUNITY",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object",
}

outputDebugString("# ----------------------------------", 'System')
outputDebugString("# Activation Pepe Tools", 'System')
outputDebugString(f"#  - author    : {bl_info['author']}", 'System')
outputDebugString(f"#  - version   : {bl_info['version']}", 'System')
outputDebugString("# ----------------------------------", 'System')

if 'bpy' in locals():
    from importlib import reload
    import sys
    for k, v in list(sys.modules.items()):
        if k.startswith(ADDON_FOLDER_NAME):
            outputDebugString(f"reload module : {v}", 'System')
            reload(v)


classes = [
    # PepeToolKet_AddonPreferences
]

register_list = [
    template,
]


def register():
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
    register()
