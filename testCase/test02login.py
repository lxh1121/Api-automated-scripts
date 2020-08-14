import json
import unittest
from common.configHttp import baserequest
import paramunittest
from Until.CryDEC import dec
import common.globalvar as gl
import common.Log
import ddt
from Until.readExcel import excel_data
from Until.codition_data import *
from Until.handle_header import *
from Until.handle_cookie import *
from Until.handle_result import *

"""
 amendment record: 2020-07-09, 新增具体接口校验具体返回值
"""

log = common.Log.logger
gl._init()
sheetname = "refund_test"
loging_xls = excel_data.get_xls('userCase.xlsx', sheetname)


@ddt.ddt
class testUserLogin(unittest.TestCase):
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
        print("测试开始前的操作")

    @ddt.data(*loging_xls)
    def testcase(self, loging_xls):
        self.caseNum = loging_xls[0]
        self.yes = loging_xls[2]  #是否执行
        self.encryption = loging_xls[5] #是否加密
        self.responseWrite = loging_xls[13] #是否写入响应data
        url = loging_xls[6]  # 请求url
        cookie = None
        get_cookie = None
        header = None
        depend_data = None
        get_headers = None
        is_head_json = None
        i = excel_data.get_rows_number(self.caseNum, sheetname)
        data1 = json.loads(loging_xls[8])  #请求参数
        if self.yes == 'yes':
            is_depend = loging_xls[3] #前置条件
            try:
                if is_depend:
                    depend_key = loging_xls[4] #依赖参数
                    data1 = assemble_data(is_depend, depend_key, data1, sheetname)
                if self.encryption == 'yes':
                    data1 = dec.encrypt(json.dumps(data1))  #需转换成标准的json格式去加解密传递
                    is_head_json = 1
                method = loging_xls[7] #请求方式

                is_header = loging_xls[10] #是否添加header
                excepect_method = loging_xls[11] #断言方式
                excepect_result = json.loads(loging_xls[12]).get("code")  #预期断言
                cookie_method = loging_xls[9] #是否添加cookie
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

                log.info("用例名称{} --- 请求api{}".format(loging_xls[1],url))
                log.info("请求参数{}".format(data1))
                print("请求参数: {}".format(data1))

                res = baserequest.run_main(method, url, data1, cookie, get_cookie, header, get_headers, is_head_json)
                if self.encryption == 'yes':
                    res = dec.decrypt(res)
                log.info("接口响应数据{}".format(res))
                print("接口响应数据{}".format(res))
                try:
                    code = res['code']
                except Exception as e:
                    res = json.loads(res)
                    code = res['code']
                    log.debug("返回数据异常：{}, 进行格式转换成功, code: {}".format(e, code))

                if self.responseWrite == 'yes':
                    excel_data.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                response_data = json.loads(loging_xls[12]).get("data")  #预期响应data
                if excepect_method == 'errorcode':
                    try:
                        if response_data != None:  #增加响应数据中具体字段断言2020-07-10
                            for key in response_data:
                                expect_value = response_data[key]
                                reality_value = get_depend_data(json.dumps(res.get('data')), key)
                                print("预期data中需断言的：{}，返回数据中的data需断言值：{}".format(expect_value, reality_value))
                                if excepect_result == code and expect_value == reality_value:
                                    excel_data.excel_write_data(i, 15, "通过")
                                else:
                                    excel_data.excel_write_data(i, 15, "失败")
                        else:
                            self.assertEqual(excepect_result, code)
                            excel_data.excel_write_data(i, 15, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 15, "失败")
                        excel_data.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        raise e
                if excepect_method == 'json': # response_data全量校验
                    if code == 1:
                        status_str = 'sucess'
                    else:
                        status_str = 'error'
                    excepect_result = get_result_json(url, status_str)
                    result = handle_result_json(res['data'], excepect_result)
                    try:
                        self.assertTrue(result)
                        excel_data.excel_write_data(i, 15, "通过")
                    except Exception as e:
                        excel_data.excel_write_data(i, 15, "失败")
                        excel_data.excel_write_data(i, 16, json.dumps(res, ensure_ascii=False))
                        raise e

            except Exception as e:
                excel_data.excel_write_data(i, 15, "失败")
                raise e

        else:
            self.skipTest('暂不执行用例--->{}'.format(loging_xls[1]))

    def tearDown(self):
        print("测试结束，输出log完结\n\n")


