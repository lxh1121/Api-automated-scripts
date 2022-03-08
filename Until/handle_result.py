#coding=utf-8
import configparser
import json
from Until.handle_json import get_value
from deepdiff import DeepDiff


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
    # dict1 = {"aaa":"AAA", "bbb":"BBBB","CC":[{"11":"22"},{"11":"44"}]}
    # dict2 = {"aaa":"123", "bbb":"BBBB","CC":[{"11":"2233"},{"11":"111"}]}
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
     # print(handle_result_json(dict1,dict2))
     # a = get_result_json("api3/newcourseskill","sucess")
     # print(base_path)
     # print(get_Path() + "/Config/result.json")