# coding=utf-8;
"""
Created on 2022/3/1 3:53 下午
Author: lxh
Project: H5的登陆 token加密规则 AES算法加解密 （padding:默认, 输出:base64，编码:utf8，秘钥:gSPs4aHZL1ocan1w）

"""
import base64
import time

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes


class CryAES:
    def __init__(self, key):
        self.key = key.encode('utf-8')


    def aesEncrypt(self, data):

        # 实例化加密套件，使用CBC模式
        cipher = AES.new(self.key, AES.MODE_ECB)
        # 对内容进行加密，pad函数用于分组和填充
        data = cipher.encrypt(pad(data.encode('utf-8'), AES.block_size))
        encrypt_data = base64.b64encode(data)        # 输出Base64格式
        return encrypt_data.decode('utf-8')
        # 将加密内容写入文件
        # file_out = open("encrypted.bin", "wb")
        # # 在文件中依次写入key、iv和密文encrypted_data
        # [file_out.write(x) for x in (self.key, cipher.iv, encrypted_data)]


if __name__ == '__main__':
    preKey = 'pretest1'
    userId = '5fc74a674fc6bc17e8d4ff82'
    mills = int(round(time.time() * 1000))
    data_cbk = "{}｜{}｜{}".format(userId, preKey, mills)
    print(data_cbk)
    dec = CryAES('gSPs4aHZL1ocan1w')
    en = dec.aesEncrypt(data_cbk)
    print(en)