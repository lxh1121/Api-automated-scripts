#coding=utf-8
from Until.handle_json import *


def get_hander():
    data = read_json("/Config/header.json")
    return data


def header_md5():
    data = get_hander()
    key = data['imooc_key']


def write_header(data,handle_key):
    fileUrl = "/Config/header.json"
    old_data = read_json(fileUrl)
    old_data[handle_key] = data
    write_value(old_data,fileUrl)