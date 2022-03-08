# coding=utf-8
from urllib.parse import unquote

import common.Log
from Until.codition_data import get_depend_data
from Until.handle_json import *
log = common.Log.Logger().logger

def get_hander():
    data = read_json("/Config/header.json")
    return data


def header_md5():
    data = get_hander()
    key = data['imooc_key']


def write_header(data=None, handle_key=None, emptys=None):
    fileUrl = "/Config/header.json"
    if emptys == 'yes':
        old_data = {}
    else:
        old_data = read_json(fileUrl)
        old_data[handle_key] = data
    write_value(old_data, fileUrl)


def get_appoint_header(header_key, response=None, is_head_json=None):
    if header_key == 'x-app-token' and response.get('data'):
        write_header(response['data']['token'], header_key)
    if header_key == 'Referer':
        page_url = get_depend_data(json.dumps(response), is_head_json)
        if page_url.startswith("caibeike://web"):
            urldecode = unquote(page_url, 'utf-8')
            prior_page = urldecode.split("url=")[1]
        else:
            prior_page = page_url
        write_header(prior_page, header_key)
    if header_key == 'wut':
        page_url = get_depend_data(json.dumps(response), is_head_json)
        cookie_data = "wut=" + page_url
        write_header(cookie_data, 'cookie')



def set_appoint_header(is_add_header):
    if is_add_header != 'no':
        return {'is_headers': is_add_header}
    else:
        return None
