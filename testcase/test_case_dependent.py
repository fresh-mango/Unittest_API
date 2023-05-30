#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import json
import unittest
import parameterized
from common.http_request import Request_Method
from utils.operate_header import Operate_Header
from utils.operate_json import Operate_Json
from utils.operate_excel import Operate_Excel
from utils.config import ParserConfig
from utils.connect_db import Operate_Mysql
from common.dependent_data import Dependent_Data
from common.get_excel_data import Get_Excel_Data
from testcase.test_login import Login_info
from utils.log import Logger


class Test_Case_dependent(unittest.TestCase):
    excel_data = Get_Excel_Data()
    case_list = excel_data.get_dependent_cases_list()



    @classmethod
    def setUpClass(cls):
        print("初始化环境,开始登录系统")
        #登录系统
        login = Login_info()
        login.login()



    @classmethod
    def tearDownClass(cls) -> None:
        print("测试结束，释放环境！")

    def setUp(self) -> None:
        self.run = Request_Method()
        self.header_info = Operate_Header()
        self.json = Operate_Json()
        self.excel = Operate_Excel()
        self.Parser = ParserConfig()
        #self.mysql = Operate_Mysql()
        self.excel_data = Get_Excel_Data()
        self.loger = Logger().get_logger()




    def tearDown(self) -> None:
        pass





    @parameterized.parameterized.expand(case_list)
    def test_case_dependent(self,*args):
        #获取依赖case_id,与被依赖case_id键值对信息
        case_ids = args[0]
        #获取依赖case_id  | #被依赖case_id
        before_case_id, after_case_id = case_ids.split(':',2)
        self.depend_data = Dependent_Data(before_case_id)
        before_case_num  =self.excel.get_rows_number(before_case_id)
        after_case_num =self.excel.get_rows_number(after_case_id)
        # 获取依赖响应数据
        depend_response_data = self.depend_data.get_data_for_key(after_case_num)
        depend_key = self.excel_data.get_depend_field(after_case_num)

        #获取被执行case的基本信息，并执行case
        base_url = self.Parser.get_url_parameter()
        api_url = self.excel_data.get_request_url(after_case_num - 1 )
        url = base_url + api_url
        method = self.excel_data.get_request_method(after_case_num - 1)
        header_form = self.header_info.get_header_data_key("Content_Type_form")
        header_json = self.header_info.get_header_data_key("Content_Type_json")
        header_format = self.excel_data.get_header_format(after_case_num - 1)
        header = header_json if header_format != 'form' else header_form
        request_data = self.excel_data.get_data_for_json(after_case_num - 1)

        # 更新依赖字段的请求信息
        request_data[depend_key] = depend_response_data
        response_data = self.run.run_main(method=method,url=url,data=request_data,headers=header)
        res = json.loads(response_data)
        self.loger.info('请求响应信息：')
        self.loger.info(res)


        #断言
        self.assertEqual(400, res['code'])
        print("被执行case的响应信息：{}，\n预期结果：{},\n实际结果：{}".format(res, 200 , res["code"]))
        # self.log.logger.debug("debug")


if __name__ == '__main__':
    unittest.main()
