import json
import unittest
import pytest
from common.configHttp import baserequest
import paramunittest
from Until.CryDEC import dec
import common.Log
from Until.readExcel import excel_data
from Until.codition_data import *
from Until.handle_header import *
from Until.handle_cookie import *
from Until.handle_result import *

log = common.Log.logger
sheetname = "login"
loging_xls = excel_data.get_xls('userCase.xlsx', sheetname)


"""
使用paramunittest 
"""
@paramunittest.parametrized(*loging_xls)
class testUserLogin(unittest.TestCase):
    def setParameters(self, caseNum, case_name, YesOrNo, precondition, relyOnKey, encryption, url, method, paraData, cookieOperate, handerOperate, assertWay, assertExpect, responseWrite, result, responseData):
        """
        :param YesOrNo: 是否执行
        :param precondition: 前置条件
        :param relyOnKey: 依赖的key
        :param encryption: 是否加密解密
        :param paraData: 请求参数（使用paramunittest必须加双引号）
        :param cookieOperate: cookie操作方式
        :param handerOperate: 请求头操作方式
        :param assertWay: 断言方式
        :param assertExpect: 预期断言
        :param result: 写入pass or  fail
        :return:
        """
        self.caseNum = str(caseNum)
        self.case_name = str(case_name)
        self.yes = str(YesOrNo)
        self.precondition = str(precondition)
        self.relyOnKey = str(relyOnKey)
        self.encryption = str(encryption)
        self.path = str(url)
        self.method = str(method)
        self.paraData = json.loads(paraData)
        self.cookieOperate = str(cookieOperate)
        self.handerOperate = str(handerOperate)
        self.assertWay = str(assertWay)
        self.assertExpect = json.loads(assertExpect)
        self.responseWrite = str(responseWrite)
        self.result = str(result)
        self.responseData = str(responseData)


    def description(self):
        """
        test report description
        :return:
        """
        pass

    def setUp(self):
        """
        Use cases perform pre-operation
        :return:
        """
        # empty_fileData("/Config/header.json")
        print("测试开始前的操作")

    def test01case(self):
        self.checkResult()

    def tearDown(self):
        print("测试结束，输出log完结\n\n")

    def checkResult(self):#断言
        """
        check test result
        :return:
        """
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        get_headers = None
        i = excel_data.get_rows_number(self.caseNum, sheetname)
        data1 = self.paraData
        if self.yes == 'yes':
            is_depend = self.precondition
            try:
                if is_depend:
                    depend_key = self.relyOnKey
                    depend_data = get_data(is_depend, sheetname)
                    data1.update({depend_key: depend_data})
                if  self.encryption == 'yes':
                    data1 = dec.encrypt(json.dumps(data1))
                    print("加密后数据{}".format(data1))
                method = self.method
                url = self.path
                is_header = self.handerOperate
                excepect_method = self.assertWay
                excepect_result = self.assertExpect.get("code")
                cookie_method = self.cookieOperate
                allowencode = self.encryption #是否解密
                if cookie_method == 'yes':
                    cookie = get_cookie_value('app')
                if cookie_method == 'write':
                    """ 必须获取cookie"""
                    get_cookie = {'is_cookie': 'aaaa'}
                if is_header == 'yes':
                    header = get_hander()
                if is_header == 'write':
                    "必须获取header"
                    get_headers = {'is_headers': 'token'}
                print(data1)
                res = baserequest.run_main(method, url, data1, cookie, get_cookie, header, get_headers, allowencode)
                print(res)
                code = res['code']
                message = res['msg']
                if excepect_method == 'mec':
                    config_message = handle_result_code(url, code)
                    try:
                        self.assertEqual(message, config_message)
                        excel_data.excel_write_data(i, 15, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 15, "失败")
                        excel_data.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        raise e
                if excepect_method == 'errorcode':
                    try:
                        self.assertEqual(excepect_result, code)
                        excel_data.excel_write_data(i, 15, "通过")
                        if self.responseWrite == 'yes':
                            excel_data.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                    except Exception as e:
                        excel_data.excel_write_data(i, 15, "失败")
                        excel_data.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        raise e
                # if excepect_method == 'json':
                #     if code == 1000:
                #         status_str = 'sucess'
                #     else:
                #         status_str = 'error'
                #     excepect_result = get_result_json(url1, status_str)
                #     result = handle_result_json(res, excepect_result)
                #     try:
                #         self.assertTrue(result)
                #         excel_data.excel_write_data(i, 13, "通过")
                #     except Exception as e:
                #         excel_data.excel_write_data(i, 13, "失败")
                #         excel_data.excel_write_data(i, 14, json.dumps(res))
                #         raise e
            except Exception as e:
                excel_data.excel_write_data(i, 15, "失败")
                raise e
