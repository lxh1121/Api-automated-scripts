#coding=utf-8
'''
Created on 2020-04-27
author: lxh
Project: 批量发布现货、报价
'''
import requests
from common.configDb import OperationMysql
import random
import datetime
from Until.CryDEC import dec
import json
host = "http://0.0.0.0:0000"


class UserIssue:
    def send_post(self, url, data, headers=None):
        re = requests.post(url=url, data=data, headers=headers)
        result = re.json()
        return result

    def send_get(self, url, data, headers=None):
        re = requests.get(url=url, params=data, headers=headers)
        result = re.json()
        return result

    def loging(self, data):
        headers = {"Content-Type": "application/json"}
        url = host + "/u"
        data1 = dec.encrypt(json.dumps(data))
        login_ = self.send_post(url, data1, headers)
        # print(login_)
        login_r = dec.decrypt(login_)
        login_new = login_r[:login_r.rfind('}')+1]
        login_res = json.loads(login_new)
        # print("登录内容-------->%s"%login_res)
        token = login_res["data"]["user"]["token"]
        token_list.append(token)
        nickName = login_res["data"]["user"]["nickName"]
        nickName_list.append(nickName)
        return token_list, nickName_list

    def productSave(self, data, headers):
        
        url = host + "/"
        res = self.send_post(url, data, headers)
        return res

    def file_multifile(self, val, headers):
        
        url = host + ""
        file = {
            "Content-Disposition": "form-data",
            "Content-Type": "image/png",
            "filename": "01.jpg",
            "multipartFile": open("E\"+ str(val) +".jpg", mode="rb")
        }
        data = {
            'decode': 1
        }
        response = requests.post(url=url, files=file, headers=headers)
        return response.json()['data']['list'][0]['id']  # 





if __name__ == '__main__':
    lxhUser = UserIssue()
    sql = OperationMysql()
    sql_two = "SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s)"
    value = ['0']
    sql_sele_data = sql.sql_select(sql_two, value)
    print(sql_sele_data)
    nowtime = str(datetime.datetime.now()).split(" ")[0]
    hour = datetime.datetime.now().hour
    phone = ["19965412404", "15888643312", "13511110000", "18803932546", "13512345678"]
    assdId = [34, 6, 9, 5, 8]
    detaild_data = [
     
    ]
    token_list = []
    nickName_list = []

    for i in range(5):
        login_data = {"account": phone[i], "password": "12345678"}
        login_res = lxhUser.loging(login_data)
        token_list = login_res[0]
        nickName_list = login_res[1]


    for n in range(30): #
        for i in range(5):
            headers = {"token": token_list[i]}
            banners = []
            val = random.randint(1, 21)
            banners.append(lxhUser.file_multifile(val,headers))
            print(banners)
            categoryId = "2000"+ str(i+1)
            model_index = 30001
            targets = json.dumps(detaild_data[i])
            price = round(random.uniform(0, 3000))
            stock = random.randint(10, 10000)
            taxRate = round(random.uniform(0, 99))
            if i == 0:
                model_index = random.randint(30001,30006)
            elif i == 1:
                model_index = random.randint(30007,30009)
            elif i == 2:
                model_index = random.randint(30010,30013)
            elif i == 3:
                model_index = random.randint(30014,30015)
            elif i == 4:
                model_index = random.randint(30016,30018)
            placeId = random.choice(sql_sele_data)[0]
            product_data = {
            }
            pur_res = lxhUser.productSave(product_data, headers)
            print("现货====>%s"%pur_res)
            # purId = lxhUser.purOrderList(1, headers)








