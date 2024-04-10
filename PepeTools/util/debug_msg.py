#!/usr/bin/python
# -*- coding: utf-8 -*-
import inspect


def outputDebugString(msg, type="Message"):
    """
    Prints a debug message with color-coded formatting.

    Args:
        msg (str): The debug message to be printed.
        type (str, optional): The type of the debug message.
            Defaults to "Message".
            Possible values for `type` are:
                - "Error": Indicates an error message.
                - "Warning": Indicates a warning message.
                - "Message": Indicates a general message.
                - "System": Indicates a system-related message.

    Returns:
        str: The debug message that was printed.
    """
    colors = {
        'Info': '\033[90m',
        'Message': '\033[37m',
        'Warning': '\033[33m',
        'System': '\033[34m',
        'Error': '\033[31m',
        'reset': '\033[37m'
    }
    caller_frame = inspect.currentframe().f_back
    caller_file = inspect.getframeinfo(caller_frame).filename.split("\\")[-1]
    caller_method = inspect.getframeinfo(caller_frame).function
    caller_line = inspect.getframeinfo(caller_frame).lineno

    print(colors[type]
          + f"[{type[:1]}] {caller_file[:16]:>16} [{caller_line:>4}] "
          + f"{caller_method[:16]:>16}() :  {msg}"
          + colors['reset'])

    return msg
