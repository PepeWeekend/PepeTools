#!/usr/bin/python
# -*- coding: utf-8 -*-
import inspect


def get_classes(modules, fileName):
    """
    指定されたモジュール内のクラスを取得するジェネレータ関数です。

    Args:
        modules: クラスを検索するモジュール
        fileName: クラスが含まれるファイル名

    Yields:
        クラスオブジェクト: 指定されたモジュール内のクラスオブジェクト

    """
    classes = inspect.getmembers(modules, inspect.isclass)
    for name, obj in classes:
        if inspect.isclass(obj) and obj.__module__ == fileName:
            yield obj
            yield from get_classes(obj, fileName)


def get_classes_of_class(modules, baseClass, fileName):
    """
    Returns a generator that yields all classes derived from `baseClass` within the specified `modules` and `fileName`.

    Args:
        modules (module or list): The module or list of modules to search for classes.
        baseClass (class): The base class to check for derived classes.
        fileName (str): The name of the file where the classes are defined.

    Yields:
        class: The derived classes found within the specified modules and file.

    """
    classes = inspect.getmembers(modules, inspect.isclass)
    derived_classes = [
        cls for name, cls in classes
        if issubclass(cls, baseClass) and cls is not baseClass
    ]

    for name, obj in derived_classes:
        if inspect.isclass(obj) and obj.__module__ == fileName:
            yield obj
            yield from get_classes_of_class(obj, baseClass, fileName)
