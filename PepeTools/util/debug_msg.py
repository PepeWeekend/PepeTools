# -*- coding: utf-8 -*-
"""PepeToolsアドオンのデバッグメッセージを提供するモジュール

説明: PepeToolsアドオンのデバッグメッセージを提供するモジュール
"""
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
    """デバッグメッセージを出力するクラス。

    Attributes:
        MsgType (Enum): メッセージの種類を表す列挙型です。
            Info: 情報メッセージ
            Message: 一般的なメッセージ
            Warning: 警告メッセージ
            System: システムメッセージ
            Error: エラーメッセージ
    """

    class MsgType(Enum):
        Info = "Info"
        Message = "Message"
        Warning = "Warning"
        System = "System"
        Error = "Error"

    def output(self, msg, msgType=MsgType.Message):
        """デバッグメッセージを出力します。

        Args:
            msg (str): 出力するメッセージ
            msgType (MsgType, optional): メッセージの種類 (デフォルトはMsgType.Message)

        Returns:
            str: 出力されたメッセージ
        """
        caller_frame = inspect.currentframe().f_back
        caller_file = inspect.getframeinfo(caller_frame).filename.split("\\")[-1]
        caller_method = inspect.getframeinfo(caller_frame).function
        caller_line = inspect.getframeinfo(caller_frame).lineno

        output_string(msgType.value, caller_file, caller_line, caller_method, msg)

        return msg


def output_string(type, fileName, line, method, msg):
    """メッセージを出力

    Args:
        type (str): メッセージの種類。'Info', 'Message', 'Warning', 'System', 'Error' のいずれか。
        fileName (str): ファイル名。
        line (int): 行番号。
        method (str): メソッド名。
        msg (str): メッセージの内容。

    Returns:
        str: 出力されたメッセージ。

    """
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
    """関数の呼び出しログを出力するデコレータ

    Args:
        func: デコレートする関数

    Returns:
        デコレートされた関数
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """
        デコレートされた関数の呼び出しログを出力します。

        Args:
            *args: 関数に渡される位置引数
            **kwargs: 関数に渡されるキーワード引数

        Returns:
            関数の実行結果
        """
        # ログ出力の処理を追加する
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} called successfully")
        return result

    return wrapper


logger = OutputDebugString()
