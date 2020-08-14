#coding=utf-8
'''
Created on 2020-04-27
author: lxh
Project: 批量签约流程
'''
import requests
import json
import random
import datetime
from Until.CryDEC import dec
import json
from common.Log import logger

host = "http://0.0.0.0:0000"

class UserSigning:
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
        login_r = dec.decrypt(login_)
        login_new = login_r[:login_r.rfind('}') + 1]
        login_res = json.loads(login_new)
        # print("登录内容-------->%s"%login_res)
        token = login_res["data"]["user"]["token"]
        token_list.append(token)
        nickName = login_res["data"]["user"]["nickName"]
        nickName_list.append(nickName)
        return token_list, nickName_list

    def purOrderList(self, state, headers):

        data = {"state": state, "pageNum": 1, "pageSize": 10}
        url = host + "/"
        res = self.send_get(url, data, headers)
        # purId = res['data']['list'][0].get('purchaseId') #采购单id
        return res

    def procurementDetail(self, purchaseId, headers):

        url = host + '/'
        data = {'purchaseId': purchaseId}
        res = self.send_get(url,data, headers)
        quotationsId = res['data']['quotationList'][0]['quotationId'] #获取一条报价id
        print(res['data']['quotationList'])
        return quotationsId

    def addAlternative(self, quotationId, headers):

        url = host + "/"
        data = {"quotationId": quotationId}
        res = self.send_post(url, data, headers)
        return res

    def initiateSign(self, data, headers):

        url = host + "/"
        res = self.send_post(url, data, headers)
        return res

    def uploadFile(self, header):
        "上传文件"
        url = host + "/"
        file = {
            "Content-Disposition": "form-data",
            "Content-Type": "application/pdf",
            "filename": "合同测试模板.pdf",
            "file": open("E:\\\合同测试模板.pdf", mode="rb")
        }
        data = {
            'decode': 1
        }
        response = requests.post(url=url, files=file, data=data, headers=header)
        return response.json()['data']['contractId'] #上传pdf合同id


    def quotationDetail(self, quotationId, headers):
        
        url = host + "/"
        data = {"quotationId":str(quotationId)}
        res = self.send_get(url, data, headers)
        return res['data']['tel']

    def supplyList(self, headers):
  
        url = host + "/"
        data = {"state": 1, "pageNum": 1, "pageSize": 10} #
        res = self.send_get(url, data, headers)
        signingId = res['data']['list'][0]['signingId'] #
        return signingId

    def getContract(self, data, headers):
        
        url = host + "/"
        res = self.send_get(url, data, headers)
        mySuppleId = res['data']['mySuppleId']  #
        myPurchaseId = res['data']['myPurchaseId'] #
        return mySuppleId, myPurchaseId

if __name__ == '__main__':
    lxhUser = UserSigning()
    phone = ["19965412404", "15888643312", "13511110000", "18803932546", "13512345678"]
    token_list = []
    nickName_list = []
    for i in range(5):
        login_data = {"account": phone[i], "password": "12345678"}
        login_res = lxhUser.loging(login_data)
        token_list = login_res[0]
        nickName_list = login_res[1]
    name_list = []
    idcard_list = [""]
    for i in range(1):
       
        headers = {'token': token_list[1]}
        is_run = lxhUser.purOrderList(2, headers=headers)
        try:
            purId = is_run['data']['list'][0].get('purchaseId')  # 
        except Exception as e:
            print("%s已经没有已截了"%phone[i])
            print("--------------------------------------------------")
            continue
        purchaseId = purId
        contractId = lxhUser.uploadFile(headers)
        quotationId = lxhUser.procurementDetail(purchaseId, headers)
        print(quotationId)
        supply_tel = lxhUser.quotationDetail(quotationId, headers) #
        addAlter = lxhUser.addAlternative(quotationId,headers)
        print("%s加入备选----->%s"%(supply_tel,addAlter))
        contract_data = {"contractId": str(contractId), "quotationId": quotationId, "enterpriseName": "甲方有限责任公司","enterpriseID": "91500000MA60515Y8F", "enterpriseIDType": 1, "corporateRepresentative": name_list[i],"accountName": "户名甲", "bankAccount": "6217920120292847", "openingBank": "浦发银行","tel": "18737553592", "email": "1771602325@qq.com", "personalIDType": 1,"personalID": idcard_list[i], "signState": 1} #身份证签约请求data
        # contract_data = {"contractId": str(contractId), "quotationId": quotationId, "enterpriseName": "甲方有限责任公司",
        #                  "enterpriseID": "91500000MA60515Y8F", "enterpriseIDType": 1,
        #                  "corporateRepresentative": "朱新妹", "accountName": "户名甲",
        #                  "bankAccount": "6", "openingBank": "浦发银行", "tel": "",
        #                  "email": "", "personalIDType": 8, "personalID": "",
        #                  "signState": 1}
        bySign = lxhUser.initiateSign(contract_data, headers) #发起签约
        print("%s发起签约---------->%s"%(phone[1], bySign))


        #
        supply_header = {"token": token_list[0]}
        signingId = lxhUser.supplyList(supply_header)
        contract_data = {"signingId":signingId, "type": 1}
        info_list = lxhUser.getContract(contract_data, supply_header)
        mySuppleId = info_list[0]  #
        myPurchaseId = info_list[1] #
        #"personalIDType": 13, "personalID": "CH0060005"
        # mysupple_data = {"enterpriseName": "乙方网络科技集团", "enterpriseID": "91440605590059829L", "enterpriseIDType": 1, "corporateRepresentative": name_list[i+1],"accountName": "户名乙", "bankAccount": "456577899877444", "openingBank": "建设银行","tel": "15703878503", "email": "3023776104@qq.com", "personalIDType": 1,"personalID": idcard_list[i+1], "id": signingId, "mySuppleId": mySuppleId, "myPurchaseId": myPurchaseId, "signState": 2} #身份证同意签约请求data
        mysupple_data = {"enterpriseName": "乙方网络科技集团", "enterpriseID": "91440605590059829L", "enterpriseIDType": 1,
                         "corporateRepresentative": "刘正权", "accountName": "户名乙",
                         "bankAccount": "", "openingBank": "建设银行", "tel": "",
                         "email": "", "personalIDType": 8, "personalID": "1026973097",
                         "id": signingId, "mySuppleId": mySuppleId, "myPurchaseId": myPurchaseId, "signState": 2}
        agreeSign = lxhUser.initiateSign(mysupple_data, supply_header) #同意签约
        print("%s同意签约---------->%s"%(supply_tel, agreeSign))
        print("--------------------------------------------------")





