#coding=utf-8
'''
Created on 2020-04-24
author: lxh
Project: 批量发布采购单(备品备件）,报价
'''
import requests
import json
import random
import datetime
host = "http://192.168.2.200:9024"

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
        url = host + "/uc/auth/access/login"
        login_res = self.send_post(url, data)
        token = login_res["data"]["user"]["token"]
        token_list.append(token)
        nickName = login_res["data"]["user"]["nickName"]
        nickName_list.append(nickName)
        return token_list, nickName_list

    def purchaseIssue(self, data, headers):
        """采购单发布"""
        url = host + "/sale/purchaseOrder/add"
        res = self.send_post(url, data, headers)
        return res

    def purOrderList(self, headers):
        "采购单列表"
        data = {"state": 0, "pageNum": 1, "pageSize": 10}
        url = host + "/sale/purchaseOrder/list"
        res = self.send_get(url, data, headers)
        purId = res['data']['list'][0].get('purchaseId')
        return str(purId)

    def quotation(self, data, headers):
        "报价"
        url = host + "/sale/quotation/add"
        res = self.send_post(url, data, headers)
        return res


if __name__ == '__main__':
    lxhUser = UserIssue()
    nowtime = str(datetime.datetime.now()).split(" ")[0]
    phone = ["18799991111", "15888643312", "13511110000", "18803932546", "13512345678"]
    assdId = [4, 2, 8, 6, 7]
    token_list = []
    nickName_list = []
    for i in range(5):
        login_data = {"account": phone[i], "password": "12345678"}
        login_res = lxhUser.loging(login_data)
        token_list = login_res[0]
        nickName_list = login_res[1]

    for n in range(1):
        for i in range(1):
            headers = {"token": token_list[i]}
            categoryId = random.randint(30022,30040)
            model_index = 0
            amount = str(random.randint(1,1000))
            pur_data = {
                "categoryId": int(categoryId), "modelId": model_index, "amount": amount, "expectedTime": nowtime,
                "stopTime": nowtime + "-12", "linkMan": nickName_list[i], "tel": phone[i],
                "addressId": assdId[i], "productType": 3, "specJson": json.dumps([{"id":1,"value":"1"},{"id":2,"value":"1"},{"id":3,"value":"1"}]), "sparePartsId": 1, "productId": 0
            }
            pur_res = lxhUser.purchaseIssue(pur_data, headers)
            print(pur_res)
            purId = lxhUser.purOrderList(headers)
            quotation_data = random.randint(1,5)
            areaIdList = [110100, 120100, 130100, 140100, 150100]
            aredId = random.sample(areaIdList, 1)[0]
            for j in range(4):
                if j == i:
                    continue
                else:
                    quoteHeaders = {"token": token_list[j]}
                    price = round(random.uniform(0,3000))
                    taxRate = round(random.uniform(0,99))
                    supplyNumber = random.randint(10,10000)
                    supplyDay = random.randint(3, 20)
                    quote_data = {"id": purId, "price": price, "linkMan": nickName_list[j], "tel": phone[j], "areaId": assdId, "targets": json.dumps([{"id":1,"value":"1"},{"id":2,"value":"1"},{"id":3,"value":"1"}]), "taxRate": taxRate, "supplyNumber": supplyNumber, "supplyDay": supplyDay, "type": 1}
                    quo_res = lxhUser.quotation(quote_data, quoteHeaders)
                    # print(quo_res)






