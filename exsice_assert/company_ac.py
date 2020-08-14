#coding=utf-8;
import requests
# from common.configDb import mysql_connet
import random
import datetime
from Until.CryDEC import dec
import json
from common.configDb import OperationMysql
# host = "http://47.102.118.32:9224"


host = "http://192.168.2.200:9024"

# /admin/org/examine  后台审核通过


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
        url = host + "/uc/auth/access/login"
        data1 = dec.encrypt(json.dumps(data))
        login_ = self.send_post(url, data1, headers)
        login_r = dec.decrypt(login_)
        login_new = login_r[:login_r.rfind('}')+1]
        login_res = json.loads(login_new)
        # print("登录内容-------->%s"%login_res)
        token = login_res["data"]["user"]["token"]
        nickName = login_res["data"]["user"]["nickName"]
        return token, nickName

    def fileUplaod(self, file_data, headers):
        url = host + '/mall/fileUpload/appUpload'
        """上传文件"""
        file = {
            "Content-Disposition": "form-data",
            "Content-Type": "application/octet-stream",
            "filename": file_data[0],
            "multipartFile": open(file_data[1], mode="rb")  # key值就是传参时name=""
        }
        response = requests.post(url=url, headers=headers, files=file)
        return response.json()

    def companAc(self, data, headers):
        "新增企业认证"
        #更新/uc/org/updateCompanyAuth
        url = host + '/uc/org/companyAuth'
        response = requests.post(url=url, data=data, headers=headers)
        return response.json()['msg']

    def orgadd(self, datajson, headers):
        "公司信息填写"
        data = {"orgJson": json.dumps(datajson)}
        url = host + '/uc/org/update'
        response = requests.post(url=url, data=data, headers=headers)
        return response.json()


if __name__ == '__main__':
    lxhUser = UserIssue()
    nowtime = str(datetime.datetime.now()).split(" ")[0]
    hour = datetime.datetime.now().hour
    phone = ["19965412404", "18803932546", "18712345678", "13511110000", "15888643312", "13512345678"]
    company_data = ["内蒙古庆华有限公司", "福建三明金属有限公司", "汉邦石化责任有限公司", "同煤广发实业有限公司", "新疆天业贸易有限公司", "赣州白塔金属有限公司"]
    token_list = []
    nickName_list = []
    for i in range(6):
        login_data = {"account": phone[i], "password": "12345678"}
        # login_data = {"account":"18803932546", "password":"12345678"}
        login_res = lxhUser.loging(login_data)
        headers = {'token': login_res[0]}
        file_iphone = ["a.jpg", "E:\\InterfaceTest\\InterfaceAuto\\exsice_assert\\a.jpg"]
        file_business = ["b.jpg", "E:\\InterfaceTest\\InterfaceAuto\\exsice_assert\\b.jpg"]
        file_data = [file_business, file_iphone]
        file_id = []
        for j in range(2):
            file_res = lxhUser.fileUplaod(file_data[j], headers)
            file_id.append(file_res['data']['id'])
        data = {"companyName": company_data[i], "idcardFile": file_id[1], "licenseFile": file_id[0], "realName": login_res[1]}
        com_res = lxhUser.companAc(data, headers)
        print("%s----%s"%(phone[i],com_res))

        #填写公司信息
        sql = OperationMysql()
        sql_two = "SELECT id FROM city_area WHERE pid in (SELECT id FROM city_area WHERE pid = %s)"
        value = ['0']
        sql_sele_data = sql.sql_select(sql_two, value)
        sql_data = sql_sele_data  # 从数据库中获取地区信息
        aredId = random.choice(sql_data).get('id')
        datajson = {"address": "找小姐姐小鸡小鸡先看下叫哦想惊喜惊喜惊喜", "businessProducts": "", "businessScope": 0, "companyType": 0,"contacts": "", "fax": "", "fileId": 0, "id": 0, "name": company_data[i], "subordinateAddress": aredId, "tel": "","wechat": ""}
        lxhUser.orgadd(datajson, headers)