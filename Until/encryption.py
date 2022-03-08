# coding=utf-8
import base64
# url 提取参数转dict
import json

import requests


class OtherUtil:
    def request_change_dict(self, res):
        res_data = res.split("&")
        new_data = {}
        for i in res_data:
            new_data[i.split("=")[0]] = i.split("=")[1]
        return json.dumps(new_data)


if __name__ == '__main__':
    from urllib.parse import urlencode
    res = "skuId=60d45f2d4fc6bc5ce292f072&buyCount=1&price=199&payAbleAmount=199&payAmount=199&couponId=&day=2022-03-07&idCard=&addressId=0&startTime=1646618400000&endTime=1646625600000"
    otherutil = OtherUtil()
    print(otherutil.request_change_dict(res))
    # URL = "caibeike://web?url=https%3A%2F%2Fpre.caibeike.net%2Fts%2Fgroupon%2Fordersubmit%3FgrouponItemId%3D4652%26trace%3Dcbk"
    # print(URL.startswith('caibeike://web'))
    # url = "https://pre.caibeike.net/trade/ajax/hotel/order/create.html"
    # # data1 = {"vo": {"itemCode": "86502727206", "trace": "cbk"}}
    # data = {"data": {"buyCount": "1", "productId": "1990", "identCode": "", "partnerInvite": "",
    #                  "roomId": "621eea6c660c35727263bc6e", "skuId": "10628", "trace": "cbk", "activityId": "",
    #                  "couponId": "0", "useCoupon": "0", "itemId": "3898772", "userId": "5fc886ed4fc6bc17e8d54078",
    #                  "soldPrice": "9", "hasAppointed": "false", "memberRebateAmount": "null", "phone": "17812121218"}}
    # # data = 'data=%7B%22buyCount%22%3A%221%22%2C%22productId%22%3A%221990%22%2C%22identCode%22%3A%22%22%2C%22partnerInvite%22%3A%22%22%2C%22roomId%22%3A%22621eea6c660c35727263bc6e%22%2C%22skuId%22%3A10628%2C%22trace%22%3A%22cbk%22%2C%22activityId%22%3A%22%22%2C%22couponId%22%3A0%2C%22useCoupon%22%3A%220%22%2C%22itemId%22%3A3898772%2C%22userId%22%3A%225fc886ed4fc6bc17e8d54078%22%2C%22soldPrice%22%3A%229%22%2C%22hasAppointed%22%3Afalse%2C%22memberRebateAmount%22%3Anull%2C%22phone%22%3A%2217812121218%22%2C%22longTermTourUserInfos%22%3A%5B%5D%7D'
    # header = {
    #     # 'x-app-token': 'T01:5i_FlSi5Mray7_o-jokDTJjJr7lVPrbl-fEun_kjUKwNM5F4evOy1NbtxyijtwoGzV4ENMNsB09b5nu8kkpqsg',
    #     'cookie': 'wut=uq9laECVM15xHpprLVBAInZVvxfibbhOvCeBiRTVxpBIMPQgcOMH36ee9UL10CpV',
    #     'Referer': 'https://pre.caibeike.net/ts/hotel/orderSubmit?productId=1990&identCode=&partnerInvite=&roomId=621eea6c660c35727263bc6e&skuId=10628&buyCount=1&trace=cbk&activityId=',
    #     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    #     # 'Content-Type': 'application/json; charset=UTF-8',
    #     'x-app-lng': '121.414246',
    #     'x-app-cityid': '5448b9fa7996edbc1d249fbc', 'x-app-locationcityid': '5448b9fa7996edbc1d249fbc',
    #     'x-app-lat': '31.209311', 'x-app-uuid': '4C277208-6D40-402E-92BE-C90A65F0343E', 'x-app-version': '4.6.7',
    #     'User-Agent': 'Caibeike/1.0(com.caibeike.android 4.6.7; M2002J9E;Android 10; 392dfe4f40342712; zh_CN)'}
    # # response = requests.post(url, json.dumps(data), headers=header)
    # response = requests.post(url, urlencode(data), headers=header)
    # print(response.text)
