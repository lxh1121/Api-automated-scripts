#coding=utf-8;
import requests
import json
from Until.CryDEC import dec
url = "http://47.102.118.32:9224/sale/signing/uploadFile"

import time
def loging(data):
    url = "http://47.102.118.32:9224/uc/auth/access/login"
    headers = {"Content-Type": "application/json"}


    data1 = dec.encrypt(json.dumps(data))
    response_login = requests.post(url=url, data=data1, headers=headers)
    print(response_login.cookies)
    login_decode = dec.decrypt(response_login.json())
    login_new = login_decode[:login_decode.rfind('}') + 1]
    login_res = json.loads(login_new)
    token = login_res["data"]["user"]["token"]
    return token

file = {
    "Content-Disposition": "form-data",
    "Content-Type": "application/pdf",
    "filename": "合同测试模板.pdf",
    "file": open("E:\\InterfaceTest\\InterfaceAuto\\exsice_assert\\合同测试模板.pdf", mode="rb")
}

data = {
    'decode': 1
}
data_login = {"account": "18803932546", "password": "12345678"}


url1 = "http://192.168.2.200:9024/mall/address/add"
headers = {"contentType": "application/json; charset=utf-8","token": "5a5354533138373337353533353932"}


adress_data = {"tel":"18737553592","areaId":110102, "areaName":"北京北京市东城区", "detailAddress":"长宁庄园2857642弄右侧大庄园", "receiveName":"路", "state":2}
response_add = requests.post(url=url1, data=adress_data, headers=headers)
print(response_add.json())
# res_login = loging(data_login)
# header = {"token": res_login}
# res = requests.post(url, files=file, data=data, headers=header)
# print(res.text)
# a = 'e2123'
# b ='asdasd'
# print("%sdsda%s"%(a,b))
import time
# import datetime
# nowtime = str(datetime.datetime.now()).split(" ")[0]
# hour = datetime.datetime.now().hour
# print(nowtime + "-" + str(hour+1))

import pymysql
import random
class mysql_connet():

    def __init__(self):
        self.conn = pymysql.connect(
            host="47.102.102.90",
            user="root",
            passwd="zsts2020",
            port=3306,
            db="zsts_news",
            charset="utf8"
        )
        self.cur = self.conn.cursor()

    def sql_execution(self,sql, val):
        self.cur.execute(sql, val)
        data = self.cur.fetchall()
        self.cur.close()
        self.conn.close()
        return data

# sql_cls = mysql_connet()
# sql = "SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s)"
# fileValue = ['0']
# sql_data = sql_cls.sql_execution(sql, fileValue)
# print(sql_data)
