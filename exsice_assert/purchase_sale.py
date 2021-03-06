#coding=utf-8
'''
Created on 2020-04-27
author: lxh
Project: 批量发布采购单和报价
'''
import requests
from common.configDb import OperationMysql
import random
import datetime
from Until.CryDEC import dec
import json

# host = "http://0.0.0.0:0000"

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
        url = host + "/"
        data1 = dec.encrypt(json.dumps(data))
        print(data1)
        login_ = self.send_post(url, data1, headers)
        # print(login_)
        login_r = dec.decrypt(login_)
        login_new = login_r[:login_r.rfind('}')+1]
        login_res = json.loads(login_new)
        print("登录内容-------->%s"%login_res)
        token = login_res["data"]["user"]["token"]
        token_list.append(token)
        nickName = login_res["data"]["user"]["nickName"]
        nickName_list.append(nickName)
        return token_list, nickName_list

    def purchaseIssue(self, data, headers):
      
        url = host + ""
        res = self.send_post(url, data, headers)
        return res

    def purOrderList(self, state, headers):
        
        data = {"state": state, "pageNum": 1, "pageSize": 10}
        url = host + ""
        res = self.send_get(url, data, headers)
        purId = res['data']['list'][0].get('purchaseId') #

    def procurementDetail(self, purchaseId, headers):
       
        url = host + '/'
        data = {'purchaseId': purchaseId}
        res = self.send_get(url,data, headers)
        # print(res)
        quotationsId = res['data']['quotationList'][0]['quotationId'] #
        return quotationsId

    def address_list(self, headers): #
        url = host + '/m'
        data = {}
        res = self.send_get(url, data, headers)
        address_id = res['data']['list'][0]['addressId']
        return address_id

    def address_add(self, data, headers): #
        url = host + '/m'
        res = self.send_post(url, data, headers)
        return True

    def quotation(self, data, headers):
 
        url = host + "/"
        res = self.send_post(url, data, headers)
        return res



if __name__ == '__main__':
    lxhUser = UserIssue()
    sql = OperationMysql()
    sql_two = "SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s)"
    value = ['0']
    sql_sele_data = sql.sql_select(sql_two, value)
    nowtime = str(datetime.datetime.now()).split(" ")[0]
    hour = datetime.datetime.now().hour
    phone = ["19965412404", "15888643312", "13511110000", "18803932546", "13512345678"]
    # assdId = [34, 6, 9, 5, 8]
    detaild_data = [
        [{"id": 1, "value": "4"}, {"id": 2, "value": "4"}, {"id": 3, "value": "4"}, {"id": 4, "value": "4"}],
        [{"id": 6, "value": "1"}, {"id": 7, "value": "4"}, {"id": 8, "value": "7"}, {"id": 9, "value": "74"},
         {"id": 10, "value": "4"}],
        [{"id": 11, "value": "1"}, {"id": 12, "value": "4"}, {"id": 13, "value": "7"}, {"id": 14, "value": "2"},
         {"id": 15, "value": "5"}, {"id": 16, "value": "8"}, {"id": 17, "value": "5"}],
        [{"id": 20, "value": "1"}, {"id": 21, "value": "4"}, {"id": 22, "value": "7"}, {"id": 23, "value": "2"},
         {"id": 27, "value": "5"}],
        [{"id": 29, "value": "1"}, {"id": 30, "value": "4"}, {"id": 31, "value": "7"}, {"id": 32, "value": "2"},
         {"id": 33, "value": "5"}, {"id": 34, "value": "8"}, {"id": 35, "value": "5"}, {"id": 36, "value": "5"},
         {"id": 126, "value": "5"}],
    ]
    token_list = []
    nickName_list = []

    for i in range(5):
        login_data = {"account": phone[i], "password": "12345678"}
        login_res = lxhUser.loging(login_data)
        token_list = login_res[0]
        nickName_list = login_res[1]

    
        aredId1 = random.choice(sql_sele_data).get('id')
        data = {}
        lxhUser.address_add(data, token_list[i])

    for n in range(20): #
         for i in range(5):
             headers = {"token": token_list[i]}
             address_id = lxhUser.address_list(headers)
             categoryId = "2000"+ str(i+1)
    #         model_index = 30001
    #         targets = json.dumps(detaild_data[i])
    #         amount = str(random.randint(1,1000))
    #         if i == 0:
    #             model_index = random.randint(30001,30006)
    #         elif i == 1:
    #             model_index = random.randint(30007,30009)
    #         elif i == 2:
    #             model_index = random.randint(30010,30013)
    #         elif i == 3:
    #             model_index = random.randint(30014,30015)
    #         elif i == 4:
    #             model_index = random.randint(30016,30018)
    #         m = random.randint(1,14)
    #         # if hour+m <= 23:
    #         #     expiration_data = nowtime+ "-" + str(hour+m)
    #         # else:
    #         #     expiration_data = nowtime+ "-" + "23"
    #         pur_data = {
    #              
    #         }
    #         # print(pur_data)
    #         pur_res = lxhUser.purchaseIssue(pur_data, headers)
    #         print("采购单====>%s"%pur_res)
    #         purId = lxhUser.purOrderList(1, headers)
    #         quotation_data = random.randint(3,5)
    #         for j in range(quotation_data):  #
    #             if j == i:
    #                 continue
    #             else:
    #                 sql_data = sql_sele_data #从数据库中获取地区信息
    #                 aredId = random.choice(sql_data).get('id')
    #                 quoteHeaders = {"token": token_list[j]}
    #                 price = round(random.uniform(0,3000))
    #                 taxRate = round(random.uniform(0,99))
    #                 supplyNumber = random.randint(10,10000)
    #                 supplyDay = random.randint(3, 20)
    #                 quote_data = {} #
    #                 quo_res = lxhUser.quotation(quote_data, quoteHeaders)
    #                 print(quo_res)







