#coding=utf-8;
import requests
import json

import time
def loging(data):
    url = "http://ops.caibeike.com/ajax/login/verifyToken.html"
    headers = {
        'Host': 'ops.caibeike.com',
        'Connection': 'keep-alive',
        'Content-Length': '209',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
        'Accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://ops.caibeike.com',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://ops.caibeike.com/ops/p/verifytoken?token=eyJzaSI6IjYyMDljYmIxZTNmMDQ1YzQ4YWEyZDk3YjZjM2NjYmIwIiwiYSI6Im9wcy13ZWIiLCJldCI6MTYxMzk5NjkzOSwibiI6OTA3OTd9.8mlUTbPnjXXNjQ7iZNUzC1d5q_4&appId=ops-web&redirect=https%3A%2F%2Fops.caibeike.com%2Findex.html',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': '_UUID=4A85D561-C0B9-406C-8358-02E40BFCE6C7; _ga=GA1.2.1944093479.1602222042; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22175177de224a79-0f5f3ff1cd8988-1f326153-1296000-175177de225ff6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22175177de224a79-0f5f3ff1cd8988-1f326153-1296000-175177de225ff6%22%7D; opsIsRememberMe=ftqGlDz71MGRS8ZgWMD1GA==; qqmail_alias=autotest@caibeike.com; SESSION=308263b9-3c9e-4ee3-961d-d4b55452f621; opsUserCookie=bMJm2WHkjRv0lY3Z0t8GE2RPejTmICVfZFpQ3YshTAo=; opsIsRememberMe=ftqGlDz71MGRS8ZgWMD1GA=='
    }

    # data1 = dec.encrypt(json.dumps(data))
    data1 = {"token":"eyJzaSI6IjNhN2FhYWEzZmZjMjQ5NWQ4NjljMTc5ZmVhYmI2ZTI5IiwiYSI6Im9wcy13ZWIiLCJldCI6MTYxMzk5OTY2NywibiI6NDM0MTh9.U3ekjUnSouaEdcoEKLQvmlj8R94", "redirect":"https://ops.caibeike.com/index.html","appId":"ops-web"}
    response_login = requests.get(url=url, params=data1, headers=headers)
    print(response_login.text)

    return
loging('a')


url = "https://ops.caibeike.com/ajax/upload/image/archive.html"

payload={}
files=[
  ('file',('壁纸集-2.zip',open('/Users/xhlu/Desktop/壁纸集-2.zip','rb'),'application/zip'))
]
headers = {
  'Host': 'ops.caibeike.com',
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
  'Accept': 'application/json',
  'Cache-Control': 'no-cache',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?0',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4421.5 Safari/537.36',
  'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryOAKjjAAZnFWevAW5',
  'Origin': 'https://ops.caibeike.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://ops.caibeike.com/tools/imageTools.html',
  'Accept-Encoding': 'gzip, deflate, br',
  'Cookie': '_UUID=4A85D561-C0B9-406C-8358-02E40BFCE6C7; _ga=GA1.2.1944093479.1602222042; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22175177de224a79-0f5f3ff1cd8988-1f326153-1296000-175177de225ff6%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22175177de224a79-0f5f3ff1cd8988-1f326153-1296000-175177de225ff6%22%7D; opsIsRememberMe=ftqGlDz71MGRS8ZgWMD1GA==; qqmail_alias=autotest@caibeike.com; SESSION=308263b9-3c9e-4ee3-961d-d4b55452f621; opsUserCookie=bMJm2WHkjRv0lY3Z0t8GE2RPejTmICVfZFpQ3YshTAo=; opsUserCookie=bMJm2WHkjRv0lY3Z0t8GE2RPejTmICVfZFpQ3YshTAo=; opsIsRememberMe=ftqGlDz71MGRS8ZgWMD1GA=='
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)


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

# import pymysql
# import random
# class mysql_connet():
#
#     def __init__(self):
#         self.conn = pymysql.connect(
#             host="47.102.102.90",
#             user="root",
#             passwd="zsts2020",
#             port=3306,
#             db="zsts_news",
#             charset="utf8"
#         )
#         self.cur = self.conn.cursor()
#
#     def sql_execution(self,sql, val):
#         self.cur.execute(sql, val)
#         data = self.cur.fetchall()
#         self.cur.close()
#         self.conn.close()
#         return data

# sql_cls = mysql_connet()
# sql = "SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s)"
# fileValue = ['0']
# sql_data = sql_cls.sql_execution(sql, fileValue)
# print(sql_data)
