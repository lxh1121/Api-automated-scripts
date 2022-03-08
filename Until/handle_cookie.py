#coding=utf-8
import json
from Until.handle_json import *


def get_cookie_value(cookie_key):
    data = read_json("/Config/cookie.json")
    return data[cookie_key]


def write_cookie(data, cookie_key):
    fileUrl = "/Config/cookie.json"
    data1 = read_json(fileUrl)
    data1[cookie_key] = data
    write_value(data1,fileUrl)


# if __name__ == "__main__":
#     get_cookie_value()