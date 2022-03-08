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



class TestAsser(unittest.TestCase):
    def testcase(self):
        if self.assertEqual(200,200,msg='false') is None:
            print("chenggong")
        else:
            print(self.assertEqual(200, 1, msg="false"))


if __name__ == '__main__':
    unittest.main()
