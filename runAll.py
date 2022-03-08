#coding=utf-8
'''
Created on 2019-11-08
author: Grayer
Project: 该项目用于接口自动化练习与熟悉
'''

# from utx import *
import os
import common.HTMLTestRunner as HTMLTestRunner
from Until.handle_header import write_header
from Until.readExcel import excel_data
from common.BeautifulReport import BeautifulReport
import getpathInfo
import unittest
from Until import readConfig
from common.configEmail import send_email
import time
import common.Log


send_email = send_email()
path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = common.Log.logger
nowDay = time.strftime('%Y-%m-%d')


class AllTest:#定义一个类AllTest
    def __init__(self):
        global resultPath
        global dayPath
        global filename
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filename = now + 'report.html'
        dayPath = os.path.join(report_path, nowDay)
        if not os.path.exists(dayPath):
            os.makedirs(dayPath)
        resultPath = os.path.join(dayPath, filename)
        self.caseListFile = os.path.join(path, 'caselist.txt')#配置执行哪些测试文件的配置文件路径
        self.caseFile = os.path.join(path, 'testCase')#真正的测试断言文件路径
        self.caseList = []
        log.info(resultPath)#将resultPath的值输入到日志，方便定位查看问题
        log.info(self.caseListFile)



    def set_case_list(self):
        """
        读取caselist.txt文件中的用例名称，并添加到caselist元素组
        :return:
        """
        fb = open(self.caseListFile)
        for value in fb.readlines():
            data = str(value)
            if data != '' and not data.startswith("#"):#如果data非空且不以#开头
                self.caseList.append(data.replace("\n", ""))
        fb.close()

    def set_case_suite(self):
        """
        读取具体测试用例
        :return:
        """
        self.set_case_list()
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in self.caseList:
            case_name = case.split("/")[-1] + ".py"
            log.info('info-casename: {}'.format(case_name))
            discover = unittest.defaultTestLoader.discover(self.caseFile, pattern=case_name, top_level_dir=None)
            suite_module.append(discover)
        if len(suite_module) > 0:
            for suite in suite_module:
                for test_name in suite:
                    test_suite.addTest(test_name)
        else:
            print('else:')
            return None
        return test_suite

    def run(self):
        """
        运行程序
        :return:
        """
        try:
            write_header(emptys='yes') #清除文件写入数据
            # 清空 resData两列数据
            rowdums = excel_data.get_rows("cbk_user.xlsx", "commodityPurchase")
            for i in range(2, rowdums + 1):
                excel_data.excel_write_data(i, 14, "", "cbk_user.xlsx")
                excel_data.excel_write_data(i, 15, "", "cbk_user.xlsx")

            suit = self.set_case_suite()
            print('try')
            if suit is not None:
                fp = open(resultPath, 'wb')
                runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='API Test Report', description='Test Description')
                runner.run(suit)
                fp.close()
            else:
                print("have no case to test")
        except Exception as ex:
            log.error("xxxxxx - 启动失败：{}".format(ex))
            print(str(ex))

        finally:
            print("***************TEST END******************")

        if on_off == 'open':
            new_report_addr = send_email.acquire_report_address('result/'+ nowDay)
            send_email.outlook(new_report_addr)
        else:
            log.info("邮件发送开关配置关闭，请打开后发送")


if __name__ == '__main__':
    AllTest().run()
