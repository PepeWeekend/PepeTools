@echo off
set ToolName=PepeTools
set BlenderVersion=4.1
set BlenderAddonPath="\Blender Foundation\Blender\"%BlenderVersion%"\scripts\addons\"
set copy_to=%AppData%%BlenderAddonPath%%ToolName%

set copy_from=%ToolName%"\*"

echo ------------------------------------------------------
echo   Start Blender Addon copy to Blender Addon folder
echo     Install Add-on Name : %ToolName%
echo ------------------------------------------------------
echo Copy to   : %copy_to%
echo Copy from : %copy_from%

xcopy %copy_from% %copy_to% /s /e /i /y
