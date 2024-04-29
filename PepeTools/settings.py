'''
This is the settings file for the PepeTools addon.
'''
TAB_NAME = "Pepe"

from PepeTools.util.debug_msg import OutputDebugString as dbg

from PepeTools.ui import template
from PepeTools.ui import restart
from PepeTools.ui import display_file_size
from PepeTools.ui import wait_set_button
from PepeTools.ui import display_model_info

'''
List of functions to enable.
'''
ENABLE_FUNCTION_LIST = [
    template,               # Display the template panel.
    restart,                # Restart the addon.
    display_file_size,      # Display the file size.
    wait_set_button,        # Set the weight.
    display_model_info      # Display the model information.
]

# Debug message outputer
logger = dbg()
