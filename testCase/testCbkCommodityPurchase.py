# coding=utf-8;
"""
Created on 2022/3/1 10:31 上午
Author: lxh
Project: cbk 商品购买流程验证

22/3/2/ 原encryption字段为加解密，现更新为提取的字段是否需要解析
"""
import unittest
from common.configHttp import baserequest
import common.globalvar as gl
import common.Log
import ddt
from Until.codition_data import *
from Until.handle_header import *
from Until.handle_cookie import *
from Until.handle_result import *

log = common.Log.logger
gl._init()
sheetname = "commodityPurchase"
excelfile = 'cbk_user.xlsx'
loging_xls = excel_data.get_xls(excelfile, sheetname)


@ddt.ddt
class testCbkCommodityPurchase(unittest.TestCase):
    def description(self):
        """
        test report description
        :return:
        """
        pass

    def setUp(self):
        """
        Use case perform pre-operation
        :return:
        """
        print("测试开始前操作")

    @ddt.data(*loging_xls)
    def testcase(self, loging_xls):

        self.caseNum = loging_xls[0]
        self.yes = loging_xls[2] #是否执行
        self.encryption = loging_xls[5] #提取的字段是否需要解析
        self.responseWrite = loging_xls[13] #是否写入响应data
        url = loging_xls[6] #请求url
        log.info("<----- 用例名称-----> {}： 请求api{}".format(loging_xls[1], url))
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        is_head_json = loging_xls[16]
        header_content_type = loging_xls[17]
        row_number = excel_data.get_rows_number(self.caseNum, excelfile, sheetname)
        data1 = json.loads(loging_xls[8]) #请求参数
        if self.yes == 'yes':
            is_depend = loging_xls[3] #前置条件
            try:
                if is_depend:
                    depend_key = loging_xls[4] #本次请求中需替换的参数
                    data1 = assemble_data(is_depend, depend_key, data1, self.encryption, excelfile, sheetname) #拼接依赖参数
                method = loging_xls[7] #请求方式
                is_add_header = loging_xls[10] #是否添加header
                excepect_method = loging_xls[11] #断言方式
                excepect_assert_data = json.loads(loging_xls[12])  #预期断言
                cookie_method = loging_xls[9] #是否添加cookie
                if cookie_method == 'yes':
                    cookie = get_cookie_value('_UUID')
                if cookie_method == 'write':
                    """ 必须获取cookie"""
                    get_cookie = {'is_cookie': 'aaaa'}

                header = get_hander() #获取请求头
                get_header_key = set_appoint_header(is_add_header)
                log.info("请求参数{}".format(data1))
                if data1.get('grouponNo'):
                    data1['grouponNo'] = None
                res = baserequest.run_main(method, url, data1, cookie, get_cookie, header, get_header_key, is_head_json, header_content_type)
                try:
                    code = res["code"]
                except Exception as e:
                    res = json.loads(res)
                    code = res["code"]
                    log.error("返回数据异常：{}, 进行格式转换成功, code: {}".format(e, code))

                if self.responseWrite == 'yes':
                    excel_data.excel_write_data(row_number, 15, json.dumps(res, ensure_ascii=False), excelfile=excelfile)
                if excepect_method == 'errorcode':
                    try:
                        for assert_key in excepect_assert_data:
                            if assert_key == "data":#预期响应data
                                for key in json.loads(loging_xls[12]).get("data"):
                                    expect_value = json.loads(loging_xls[12]).get("data")[key]
                                    reality_value = get_depend_data(json.dumps(res.get('data')), key)
                                    if self.assertEqual(expect_value, reality_value,msg=key + "预期不匹配") is None:
                                        excel_data.excel_write_data(row_number, 14, "通过", excelfile=excelfile)
                                    else:
                                        excel_data.excel_write_data(row_number, 14, "失败", excelfile=excelfile)
                                        break
                            elif self.assertEqual(excepect_assert_data.get(assert_key), res.get(assert_key), msg=assert_key+"预期不匹配") is None:
                                excel_data.excel_write_data(row_number, 14, "通过", excelfile=excelfile)
                            else:
                                excel_data.excel_write_data(row_number, 14, "失败", excelfile=excelfile)
                                break
                    except Exception as e:
                        excel_data.excel_write_data(row_number, 15, json.dumps(res, ensure_ascii=False), excelfile=excelfile)
                        raise e
                if excepect_method == 'json': # response全量校验
                    if code == 1:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_all_data = get_result_json(url, status_str)
                    result = handle_result_json(res['data'], excepect_all_data)
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(row_number, 14, "通过", excelfile=excelfile)
                    except Exception as e:
                        excel_data.excel_write_data(row_number, 14, "失败", excelfile=excelfile)
                        excel_data.excel_write_data(row_number, 15, json.dumps(res, ensure_ascii=False), excelfile=excelfile)
                        log.error(e)
                        raise e
            except Exception as e:
                excel_data.excel_write_data(row_number, 14, "失败", excelfile=excelfile)
                log.error(e)
                raise e

        else:
            self.skipTest('暂不执行用例--->{}'.format(loging_xls[1]))

    def tearDown(self):
        print("测试结束，输出log完结\n\n")