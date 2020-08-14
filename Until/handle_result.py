#coding=utf-8

from Until.handle_json import get_value
from deepdiff import DeepDiff
"""
Greated to 2020-05-24
author: Sunwalker
effect: 增加响应数据存储，对返回数据进行全量校验
"""


def handle_result_code(url, code):
    code_path = "/Config/code_message.json"
    data = get_value(url, code_path)
    if data != None:
        for i in data:
           message = i.get(str(code))
           if message:
               return message
    return None


def respons_result(exc_result,code):
    for i in eval(exc_result):
        message = i.get(code)
        if message:
            return message
    return None


def get_result_json(url, status):
    json_path = "/Config/result.json"
    data = get_value(url, json_path)
    if data != None:
        for i in data:
            message = i.get(status)
            if message:
                return message
    return None


def handle_result_json(dict1,dict2):
    """
    校验格式json
    :return:
    """
    if isinstance(dict1,dict) and isinstance(dict2,dict):

        cmp_dict = DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        if cmp_dict.get('dictionary_item_added'):
            return False
        else:
            return True
    return False


if __name__ == "__main__":
     # a = handle_result("api3/getbanneradvertver2", '10002')
     dict1 = {"aaa":"AAA", "bbb":"BBBB","CC":[{"11":"22"},{"11":"44"}]}
     dict2 = {"bbb":"BBBB","CC":[{"11":"2233"},{"11":"111"}]}
