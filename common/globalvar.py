#!/usr/bin/python
# -*- coding: utf-8 -*-

def _init():
    global _global_dict
    _global_dict = {}

def set_value(name, value):
    """
    设置全局变量赋值，方便其他接口调用（如token）之类的值
    :param name:
    :param value:
    :return:
    """
    _global_dict[name] = value

def get_value(name, defValue=None):
    try:
        return _global_dict[name]
    except KeyError:
        return defValue

