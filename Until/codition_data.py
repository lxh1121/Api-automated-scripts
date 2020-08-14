#coding=utf-8
import os
import sys
from Until.readExcel import excel_data
from jsonpath_rw import parse
import json
"""
Greated to 2020-04-31
author: Sunwalker
effect: 新增上下游接口依赖参数传递
"""
base_path = os.path.abspath('..')
sys.path.append(base_path)


def split_data(data):
    """分割字符，取出要获取返回数据的case名称和要取的返回值"""
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def depend_data(data, sheetname):
    """获取依赖结果集-返回数据"""
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id, sheetname)
    data = excel_data.get_cell_value(row_number,16, sheetname)
    return data


def get_depend_data(res_data, key):
    """获取依赖字段的值"""
    res_data = json.loads(res_data)
    json_exe = parse(key)
    madle= json_exe.find(res_data)
    return [math.value for math in madle][0]


def get_data(data, sheetname):
    res_data = depend_data(data, sheetname)
    rule_data = split_data(data)[1]
    return get_depend_data(res_data, rule_data)


def request_data_key_update(key, value):
    """
    请求参数中key替换
    :param key:
    :param value:
    :return:
    """


def assemble_data(update_data, update_key, request_data, sheetname):
    """
    组装参数，把需要更新的参数进行更新替换
    :param update_data: 上个接口的返回数据，作为当前接口更新使用
    :param update_key: 请求数据中需更新的参数
    :param request_data: 当前接口请求数据
    :return:
    """
    split_data = update_data.split(",")
    split_key = update_key.split(",")
    for i in range(len(split_data)):
        key = split_key[i]
        value = get_data(split_data[i], sheetname)
        request_data.update({key: value})
    return request_data


if __name__ == "__main__":

    test_data = "imooc_006>data.user.headImg"
    data1 = {}
    depend_key = "token, id"
    print(test_data.split(","))
    # print(get_data(test_data, 'a')
    # print(assemble_data(test_data, depend_key, data1))