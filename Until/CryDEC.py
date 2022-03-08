import base64
import time

from Crypto.Cipher import DES
import binascii
import json
import ast
import requests
"""
Created to 2020-05-12
author: Grayer
effect: DES下ECB模式的加密解密规则（padding:pkcs7, 输出:hex，编码:utf8，秘钥:rZKOc9$^PI^dEDyA）
"""


class CryDEC:
    def __init__(self, key):
        self.key = key.encode('utf8')
        self.dec = DES.new(self.key, DES.MODE_ECB)
        self.bs = DES.block_size

    def add_to_16(text):
        while len(text) % 8 != 0:
            text += '\0'
        return text

    def encrypt(self, data):
        "dec加密"
        bs =  self.bs
        pad = lambda s: s + (bs - len(s) % bs) * chr(bs - len(s) % bs)
        cipher = self.dec
        data = cipher.encrypt(pad(data).encode('utf8'))
        # encrypt_data = binascii.b2a_hex(data)  # 输出hex格式
        encrypt_data = base64.b64encode(data)         # 取消注释，输出Base64格式
        return encrypt_data.decode('utf8')

    def decrypt(self, decrData):
        "dec解密"
        cipher = self.dec
        plain_text = cipher.decrypt(binascii.a2b_hex(decrData))
        plain_decode = plain_text.decode('utf8')
        return plain_decode[:plain_decode.rfind('}')+1] #去除解密后末尾后生成的特殊字符


key = 'rZKOc9$^'
dec = CryDEC(key)

if __name__ == '__main__':
    data = "{}"
    key = 'gSPs4aHZL1ocan1w'  # 因为该模式下秘钥要求8位，所以直接取前8位进行加密
    dec = CryDEC(key)
    en = dec.encrypt(json.dumps(data))
    print(en)
    headers = {"Content-Type": "application/json"}



    # res_login = requests.post("http://47.102.118.32:9224/uc/auth/access/login", data=en, headers=headers)
    # print("response返回的加密data：{}".format(res_login.content))
    # pas = dec.decrypt(res_login.json())
    # print('--------------------------------------')
    # print("响应data解密后：{}".format(json.loads(pas)))
    # pas2 = json.loads(pas)  #解密后，字符串末尾有特殊字符需要处理，但在pycharm中显示空白符，所以实际不是空白，只是显示问题
    # a = ""
    # print(ord(a))  #ascii码是4   字符是EOT





    #解决json.decoder.JSONDecodeError: Extra data: line 1 column 493 (char 492)
    #http://www.chenxm.cc/article/76.html