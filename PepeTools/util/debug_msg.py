#!/usr/bin/python
# -*- coding: utf-8 -*-
import inspect
from enum import Enum
import functools


def outputDebugString(msg, type="Message"):
    #
    # 利用しない方向で修正する
    #
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
    caller_frame = inspect.currentframe().f_back
    caller_file = inspect.getframeinfo(caller_frame).filename.split("\\")[-1]
    caller_method = inspect.getframeinfo(caller_frame).function
    caller_line = inspect.getframeinfo(caller_frame).lineno

    output_string(type, caller_file, caller_line, caller_method, msg)

    return msg


class OutputDebugString:
    class MsgType(Enum):
        Info = "Info"
        Message = "Message"
        Warning = "Warning"
        System = "System"
        Error = "Error"

    def output(self, msg, msgType=MsgType.Message):
        caller_frame = inspect.currentframe().f_back
        caller_file = inspect.getframeinfo(caller_frame).filename.split("\\")[-1]
        caller_method = inspect.getframeinfo(caller_frame).function
        caller_line = inspect.getframeinfo(caller_frame).lineno

        output_string(msgType.value, caller_file, caller_line, caller_method, msg)

        return msg


def output_string(type, fileName, line, method, msg):
    colors = {
        'Info': '\033[90m',
        'Message': '\033[37m',
        'Warning': '\033[33m',
        'System': '\033[34m',
        'Error': '\033[31m',
        'reset': '\033[37m'
    }
    print(colors[type]
          + f"[{type[:1]}] {fileName[:16]:>16} [{line:>4}] "
          + f"{method[:16]:>16}() :  {msg}"
          + colors['reset'])

    return msg


def call_log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        caller_frame = inspect.currentframe().f_back
        caller_file = inspect.getframeinfo(caller_frame).filename.split("\\")[-1]
        caller_method = inspect.getframeinfo(caller_frame).function
        caller_line = inspect.getframeinfo(caller_frame).lineno
        define_file = inspect.getsourcefile(func).split('\\')[-1]
        define_line = inspect.getsourcelines(func)[1]
        output_string("Info", caller_file, caller_line, caller_method, f"to {define_file} [{define_line:>4}] : args {args}")
        return func(*args, **kwargs)
    return wrapper
