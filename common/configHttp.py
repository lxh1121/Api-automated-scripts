#coding=utf-8
from urllib.parse import unquote, urlencode

import requests
import common.Log
from urllib3 import encode_multipart_formdata
from Until.handle_cookie import write_cookie
from Until.handle_header import *
from Until.geturlParams import geturlParams
from Until.codition_data import get_depend_data

log = common.Log.Logger().logger
domain_name = geturlParams.get_Url('mapi')
h5_name = geturlParams.get_Url('h5')

class BaseRequest:
    def send_post(self, url, data, cookie=None, get_cookie=None, header=None, get_headers=None, is_head_json=None):
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
                response = requests.post(url=url, headers=headers_from_data, data=file_data)
        else:
            log.info("传递后header：{}".format(header))
            response = requests.post(url=url, data=data, headers=header, cookies=cookie)
            log.info("接口响应数据{}，响应码{}".format(response.text, response.status_code))

            if get_cookie is not None:
                cookie_value_jar = response.cookies
                cookie_value = requests.utlis.dict_from_cookiejar(cookie_value_jar)
                write_cookie(cookie_value, get_cookie['is_cookie'])
            if get_headers is not None:
                # 加解密
                # re = dec.decrypt(response.json())
                # re_filter = re[:re.rfind('}') + 1]
                # response_dec = json.loads(re_filter)
                get_appoint_header(get_headers['is_headers'], response.json(), is_head_json)

        res = response.text
        return res

    def send_get(self, url, data, cookie=None, get_cookie=None, header=None, get_headers=None, is_header_json=None):
        print("传递后header：{}".format(header))
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)
        if get_cookie != None:
            cookie_value_jar = response.cookies
            cookie_value = requests.utils.dict_from_cookiejar(cookie_value_jar)
            write_cookie(cookie_value, get_cookie['is_cookie'])
        res = response.text
        return res

    def run_main(self, method, url, data, cookie=None, get_cookie=None, header=None, get_headers=None, is_head_json=None, header_content_type=None):
        # return get_value(url)
        # base_url = handle_ini.get_value('host')
        # if 'http' not in url:
        #     url = base_url + url
        # if is_head_json == 1:
        if header == None:
            header = {
                'x-app-lng': '121.414246',
                'x-app-cityid': '5448b9fa7996edbc1d249fbc',
                'x-app-locationcityid': '5448b9fa7996edbc1d249fbc',
                'x-app-lat': '31.209311',
                'x-app-uuid': '4C277208-6D40-402E-92BE-C90A65F0343E',
                # 'host': 'mapi.caibeike.net',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-app-version': '4.6.7',
                'User-Agent': 'Caibeike/1.0(com.caibeike.android 4.6.7; M2002J9E;Android 10; 392dfe4f40342712; zh_CN)'
            }
        else:
            header.update({
                'x-app-lng': '121.414246',
                'x-app-cityid': '5448b9fa7996edbc1d249fbc',
                'x-app-locationcityid': '5448b9fa7996edbc1d249fbc',
                'x-app-lat': '31.209311',
                'x-app-uuid': '4C277208-6D40-402E-92BE-C90A65F0343E',
                # 'host': 'mapi.caibeike.net',
                'Content-Type': 'application/x-www-form-urlencoded',
                'x-app-version': '4.6.7',
                'User-Agent': 'Caibeike/1.0(com.caibeike.android 4.6.7; M2002J9E;Android 10; 392dfe4f40342712; zh_CN)'
            })
        if header_content_type:
            header['Content-Type'] = "application/json; charset=UTF-8"
            data = json.dumps(data)
            url = h5_name + url
        else:
            url = domain_name + url
            data = urlencode(data)
        if method == 'get':
            res = self.send_get(url, data, cookie, get_cookie, header, get_headers, is_head_json)
        else:
            res = self.send_post(url, data, cookie, get_cookie, header, get_headers, is_head_json)
        try:
            res = json.loads(res)
            s = requests.session()
            s.keep_alive = False
        except:
            print('这个结果是一个text')
        return res



baserequest = BaseRequest()

if __name__ == '__main__':
    request = BaseRequest()
    request.run_main('get', 'login',"{'username':'111111'}")
