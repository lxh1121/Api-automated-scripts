#coding=utf-8
import os
import sys
from urllib.parse import unquote
import common.Log

log = common.Log.logger

base_path = os.path.abspath('..')
sys.path.append(base_path)
from Until.readExcel import excel_data
from jsonpath_rw import parse
import json


def split_data(data):
    """分割字符，取出要获取返回数据的case名称和要取的返回值"""
    case_id = data.split(">")[0]
    rule_data = data.split(">")[1]
    return case_id, rule_data


def depend_data(data, excelfile, sheetname):
    """获取依赖结果集-返回数据"""
    case_id = split_data(data)[0]
    row_number = excel_data.get_rows_number(case_id, excelfile, sheetname)
    data = excel_data.get_cell_value(row_number,15, excelfile, sheetname)
    return data


def get_depend_data(res_data, key):
    """获取依赖字段的值"""
    res_data = json.loads(res_data)
    json_exe = parse(key)
    madle= json_exe.find(res_data)
    if madle:
        return [math.value for math in madle][0]
    else:
        return None


def get_data(depledata_split, excelfile, sheetname):
    res_data = depend_data(depledata_split, excelfile, sheetname)
    key_path = split_data(depledata_split)[1]
    return get_depend_data(res_data, key_path)


def request_data_key_update(key, value):
    """
    请求参数中key替换
    :param key:
    :param value:
    :return:
    """
    pass


def assemble_data(update_data, update_key, request_data, encryption, excelfile, sheetname):
    """
    组装参数，把需要更新的参数进行更新替换
    :param update_data: 要更换的参数key在上一个响应中的路径
    :param update_key: 本次请求数据中需更新的key
    :param request_data: 当前接口请求request
    ：prarm encryption: 更换后的value需要解析出该参数对应的值
    :return:
    """
    try:
        depledata_split = update_data.split(",")
        split_key = update_key.split(",")
        for i in range(len(depledata_split)):
            key = split_key[i]
            value = get_data(depledata_split[i], excelfile, sheetname)
            if key in request_data:
                request_data.update({key: value})
            elif "vo" in request_data:
                request_data['vo'].update({key:value})
            elif "data" in request_data:
                request_data['data'].update({key:value})

        if request_data.get(encryption): #暂只支持从响应数据的url中更新一种key
            decode_url = request_data.get(encryption)
            if decode_url.startswith("caibeike://web"):
                decode_url = unquote(decode_url, 'utf-8') #url解码
                log.info("解析后url {}".format(decode_url))
            for i in decode_url.split('?')[len(decode_url.split('?')) - 1].split('&'):
                if i.find(encryption) != -1:
                    log.info("url中需要获取的参数: {}".format(i))
                    request_data[encryption] = i.split('=')[1]
    except Exception as e:
        log.error(e)
        log.error("报错信息{}, 需更新的key：{}, URL中需解析的key:{}, 未更新的请求数据：{}".format(e, update_key, encryption, request_data))
    return request_data


if __name__ == "__main__":

    test_data = "{'sa':'a'}"
    data = {
        "aaa":None,
        "vvv":"cccc",
        "ad":[{
            "ww":1,
            "cc":"po"
        },{
            "ee":2,
            "vb":"lk"
        }

        ]
    }
    data.update({"vvv":"tttt"})
    print(get_depend_data(json.dumps(data), 'ad[0].ww'))

    decode_url = 'https://pre.caibeike.net/pay/cashier/dispatch?orderNo=Q616954136970&payOrderNo=236911776296337408'
    # if decode_url.startswith("caibeike://web"):
    #     decode_url = unquote(decode_url, 'utf-8')  # url解码
    #     log.info("解析后url {}".format(decode_url))
    # for i in decode_url.split('?')[len(decode_url.split('?')) - 1].split('&'):
    #     if i.find("payOrderNo") != -1:
    #         log.info("url中需要获取的参数: {}".format(i))
    #         print(i.split('=')[1])
    # print(test_data.split(","))
    # print(get_data(test_data, 'a')
    # print(assemble_data(test_data, depend_key, data1))
