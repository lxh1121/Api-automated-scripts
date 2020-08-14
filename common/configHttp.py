#coding=utf-8
import requests
import json
import common.Log
from urllib3 import encode_multipart_formdata
from Until.handle_json import get_value
from Until.handle_cookie import write_cookie
from Until.handle_header import *
from Until.geturlParams import geturlParams
from Until.CryDEC import dec
log = common.Log.Logger().logger
domain_name = geturlParams.get_Url()


class BaseRequest:
    def send_post(self, url, data, cookie=None, get_cookie=None, header=None, get_headers=None):
        url1 = domain_name + url
        if geturlParams.fileUploadSplit(url) == "fileUpload":
            with open(data["filepath"], mode="rb")as f:  # 打开文件
                file = {
                    "multipartFile": (data["filename"], f.read())  # 引号的file是接口的字段，后面的是文件的名称、文件的内容,如果接口中有其他字段也可以加上
                }
                encode_data = encode_multipart_formdata(file)
                file_data = encode_data[0]
                headers_from_data = {
                    "Content-Type": encode_data[1]
                }
                response = requests.post(url=url1, headers=headers_from_data, data=file_data)
        else:
            print("传递后header：{}".format(header))
            response = requests.post(url=url1, data=data, headers=header, cookies=cookie)
            if get_cookie != None:
                cookie_value_jar = response.cookies
                cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
                write_cookie(cookie_value, get_cookie['is_cookie'])
            if get_headers != None:
                re = dec.decrypt(response.json())
                re_filter = re[:re.rfind('}') + 1]
                response_dec = json.loads(re_filter)
                if response_dec['data']['user']['token']:
                    write_header(response_dec['data']['user']['token'], get_headers['is_headers'])
                    write_header("20", 'roleId')
                else:
                    print('token不存在')
        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None, header=None, get_headers=None):
        print("传递后header：{}".format(header))
        url1 = domain_name + url
        response = requests.get(url=url1, params=data, cookies=cookie, headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None, get_headers=None, is_head_json=None):
        if is_head_json == 1:
            if header == None:
                header = {"Content-Type": "application/json; charset=utf-8"}
            else:
                header.update({"Content-Type": "application/json; charset=utf-8"})

        if method == 'get':
            res = self.send_get(url, data, cookie, get_cookie, header, get_headers)
        else:
            res = self.send_post(url, data, cookie, get_cookie, header, get_headers)
        try:
            res = json.loads(res)
        except:
            print('这个结果是一个text')
        return res



baserequest = BaseRequest()

if __name__ == '__main__':
    request = BaseRequest()
    request.run_main('get', 'login',"{'username':'111111'}")
