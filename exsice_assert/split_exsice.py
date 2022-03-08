import urllib.parse

from logzero import xrange

"""
url = 'http://192.168.0.10:9024/uc/auth/access/login?account=18737553592&password=123456'
data1 = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(url).query))
# print(data1)

list_filt = data1.keys()
#
# for k,v in data1.items():
#     data1[k] = int(v)
#     # print(data1[k], type(data1[k]))

import os
import sys


path = os.path.split(os.path.realpath(__file__))[0]
report_path = os.path.join(path, 'result')
new_path = os
print(path)
print(report_path)
print(new_path)
print(sys.argv[0])
print(os.path.basename(__file__))
"""


import requests
'''
host = 'http://192.168.0.219:9024'
url_login = '/uc/auth/access/login'
url1 = '/mall/goods/list'
api_responce = requests.post(host+url_login,data={'account':'18737553592', 'password':'123456'})
# print(api_responce.json()['data']['user']['token'])
headers = {'Content-Type':'application/x-www-form-urlencoded', 'token': api_responce.json()['data']['user']['token']}
# goods_list = requests.post(host+url1, headers=headers)
# print(goods_list.json()['data']['list'][1])
# print(type(goods_list.json()['data']['list']))
#
# url2 = '/mall/goods/detail'
# goods_detail = requests.get(host+url2, params={'spuId': 193},headers=headers)
# print(goods_detail.json())
# headers = {'token': '5a5354533138373337353533353932'}
url3 = '/mall/order/confirm'
order = requests.post(host+url3, data={'shopIds':'[43]'}, headers=headers)
print(order.json())
'''


# a = {'name':'a', 'pas':123}
# print(type(a))
# print(list(a.values())[0])
#
# b = {"orderJson":'{"list":[{"deliveryId":"0","shopId":"43","remarks":"","skuList":[{"skuId":20,"count":3}]}],"existCart":2,"addressId":432}'}
# print(type(b))
# c = eval(str(b))
# print(type(c['orderJson']))

import random
#
# token = []
# for i in range(5):
#     token.append(i)
#     print(token)
#     print(type(i))
lis= [30,34,39,41,53]
print(random.sample(lis,1))
print(type(random.sample(lis,1)))

# dict_1 = {'addressInfo': '湖北省 省直辖县级行政区划', 'amount': 144.0, 'unit': '吨', 'modelId': 30010, 'createTime': '2020-04-24', 'purchaseId': 1253577070986960970, 'stopTime': '2020-04-24 15:00:00', 'state': 3, 'categoryName': '特级 煤沥青', 'categoryId': 20003, 'productType': 1}
#
# print(dict_1.get('unit'))
# print(round(random.randint(1,4),2))
# for i in range(1):
#     print(i)
# import datetime
#
# datime = datetime.datetime.now()
# print(str(datime))
#
# print(str(datime).split(" ")[0])


# import requests
# data = {'account': '18821212121'}
# res = requests.post("http://192.168.2.200:9024/mall/fileUpload/appUpload", data)
# print(res.text)

# def url_spilt(url):
#     com_para = url.split("/")
#     return com_para
#
# url1 = url_spilt("/mall/fileUpload/appUpload")
# url2 = url_spilt("/mall/fileUpload/manyFormatUpload")
# print(url1)
# print(url2)
#
# a = {"token": "12312321313"}
# b = None
#
# from ruamel import yaml
# from getpathInfo import get_Path
#
# desired_caps = {
#     'platformName': 'Android',
#     'platformVersion': '7.0',
#     'deviceName': 'A5RNW18316011440',
#     'appPackage': 'com.tencent.mm',
#     'appActivity': '.ui.LauncherUI',
#     'automationName': 'Uiautomator2',
#     'unicodeKeyboard': True,
#     'resetKeyboard': True,
#     'noReset': True,
#     'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
# }
#
#
# data = {
#     "name": "huihui",
#     "age": 18
# }

list1 = ['123', 23, 2132]
# path = get_Path() + "/Config/a.yaml"
# with open(path, 'a', encoding='utf-8') as f:
#     yaml.dump(list1, f, Dumper=yaml.RoundTripDumper)
# from jsonpath_rw import parse
# test_data = 'data.banner.id'
# # yaml.dump()
# print(parse(test_data))
#
# da = {"a": 1}
# da1 = [1, 2, 3]
# da2 = '123'
# print(random.choice(da2))
#
# import time
# print(time.strftime("%Y%m%d-%H%M%S"))
print("---------------------------")
# num = 10
# _dict1 = dict([(i, i) for i in xrange(num)])



res = "chooseBuyType=0&activityId=&buyCount=1&grouponItemId=4652&idCardNo=&itemId=621edfb94fc6bc1bee4ded2c&price=65&payAmount=65&useCoupon=false&refToken=&storeId=&storeName=&skuId=&startDate=0&endDate=0&trace=cbk&firstPlayerFree=false&couponId=&unPaid39Order=false&unPaidOrder=false&directBuy=false&phone=&groupMode=false"
res_data = res.split("&")
print(res_data)
new_data = {}
for i in res_data:
    new_data[i.split("=")[0]] = i.split("=")[1]

print(new_data)
from Until.codition_data import *
verify_data = {"code": 1, "data":{"list":[{"action":1}], "map": "abc"}}
res_one = {"code": 1, "data":{"list":[{"action":1, "url": "dasdsa", "ad": 2132}, {"action344":3, "url44": "dasdsa", "ad1122": 1111, 'zxcc':123}], 'ad':111}}
verify_data1 = {"code": 1,}
c_data = "{'data':2312}"
up_key = "list[0].action"
res_two = {"list":[{"action":1, "url": "dasdsa", "ad": 2132}, {"action344":3, "url44": "dasdsa", "ad1122": 1111, 'zxcc':123}], 'ad':111}
key_split_data = up_key.split(".")
print(res_one.keys())
key_list = ['list', 0, 'action']
i = 3
    # if isinstance(key_list[i], str):
# res_two[key_list[i-i]][key_list[i-i+1]] = 'zxc'
# for key in res_two.keys():
def key_ee(key, value, data):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                data[key] = value
                return True
            else:
                if isinstance(v, dict):
                    key_ee(key, value, v)
                if isinstance(v, list):
                    key_ee(key, value, v)
                else:
                    return False
    if isinstance(data, list):
        for i in data:
            if isinstance(i, dict):
                key_ee(key, value, i)
            if isinstance(i, list):
                key_ee(key, value, i)
            else:
                return False
re1 = {'list': [[{'action': '111', 'url': 'dasdsa', 'ad': 2132}], {'action344': 3, 'url44': 'dasdsa', 'ad1122': 1111, 'zxcc': 123}], 'ad': 111}
a = key_ee('action', '123213', re1)
print(a)
print(re1)


def key_get(key, value, data):
    for k,v in res_two.items():
        if k == key:
            data[key]= value
            return True
        else:
            if isinstance(v, dict):
                key_get(key, value, v)
            if isinstance(v, list):
                for i in v:
                    for k1, v1 in i.items():
                        if k1 == key:
                            i[key] = value
                            return True
            else:
                return False
    # return True

# for i in range(3):
#     r_str = res_two[i]

# for i in range(len(key_split_data)):
#     key = key_split_data[i]
#
#     if key.find('[') != -1:
#         key_one = key.split("[")
#         print(key_one)
#         # res_two = res_two[key_one[0]][key_one[1].split(']')[0]]
#         key1 = key_one[0]
#         key2 = key_one[1].split(']')[0]
#         key_list.append(key1)
#         key_list.append(int(key2))
#     else:
#         key_list.append(key)
#     print(key_list)


# res_data = {"list":[{"action":1}], "map": "abc"}
res_data = {"ad": 1}

from urllib.parse import unquote
url = 'caibeike://web?url=https%3A%2F%2Fpre.caibeike.net%2Fts%2Fgroupon%2Fordersubmit%3FgrouponItemId%3D4652%26trace%3Dcbk'
urlden = unquote(url, 'utf-8')
print(urlden)
for i in urlden.split('?')[len(urlden.split('?'))-1].split('&'):
    if i.find("groupon") != -1:
        print(i.split('=')[1])
# try:
#     ve_data = verify_data.get('data')
#     # v = c_data['data']
#     print("++++++++++++++")
# except :
#     print("跳出")
# ve_data = verify_data.get('data').get("list")
# data_dict = res_one.get('data').get('list')
# print(type(data_dict))
# if type(data_dict) == list:
#     print(len(data_dict))
# print(get_depend_data(json.dumps(res_one.get('data')), "list.[0].action"))
# a = '"asd":"asd"'
# b = '{\n"zxc":"azd",\n "asd": "asd"\n}'
# if a in b:
#     print('a')
# else:
#     print('b')

# if ve_data != None:
#     if len(ve_data) != 0:
#         for key in ve_data:
#             # a = res_one.get("data").get(key)
#             a = get_depend_data(json.dumps(res_one.get("data")), key)
#             b = ve_data.get(key)
#             print(a, b)
# else:
#     print("不存在data参数")

# Python遍历dict的key最高效的方法是什么？
# 直接遍历dict for key in dict,  dict.iterkeys()

