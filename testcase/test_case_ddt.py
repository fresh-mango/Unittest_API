#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import unittest
import json
import ddt
import os

from common.http_request import Request_Method
from common.get_excel_data import Get_Excel_Data
from utils.operate_header import Operate_Header
from utils.operate_json import Operate_Json
from utils.operate_excel import Operate_Excel
from utils.config import ParserConfig,expect_result_path
from utils.connect_db import Operate_Mysql
from testcase.test_login import Login_info
from utils.log import Logger


@ddt.ddt
class Test_Case_ddt(unittest.TestCase):
    excel_data = Get_Excel_Data()
    case_list = excel_data.get_general_case()

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
        self.expect_json = Operate_Json(expect_result_path)
        self.excel = Operate_Excel()
        self.Parser = ParserConfig()
        self.mysql = Operate_Mysql()
        self.loger = Logger().get_logger()




    def tearDown(self) -> None:
        pass

    @ddt.data(*case_list)
    @ddt.unpack

    def test_case(self,case_id=None,api_name=None,case_name=None,priority=None,is_run=None,pre_condition=None,data_depend=None,
                      field_depend=None,url=None,request_method=None,format_type=None,request_key=None,operate_cookie=None,
                      operate_header=None,expect_mode=None,expect_key=None,actual_result=None,diary_data=None,remark=None):


        #执行数据库操作,SQL增删改查
        if is_run == 'init':
            init_expect_key = self.json.get_data(request_key)
            inin_data = self.mysql.sql_execute(init_expect_key)
            if 'OK,SQL命令执行成功' == inin_data:
                print("当前执行用例编号【{}】,请求数据关键字key：{},\n请求数据：{},\n实际结果：{}".format(case_id,request_key,init_expect_key,inin_data))


        else:
            header_form = self.header_info.get_header_data_key("Content_Type_form")
            header_json = self.header_info.get_header_data_key("Content_Type_json")
            header_format = format_type
            header = header_json if header_format != 'form' else header_form
            response = self.run.run_main(url=self.Parser.get_url_parameter() + url, method=request_method,
                                         data=json.dumps(self.json.get_data(request_key)), headers=header)

            res = json.loads(response)
            self.loger.info('请求响应信息：')
            self.loger.info(res)
            expect_result = self.expect_json.get_data(expect_key)
            self.assertEqual(expect_result,res)
            print("当前执行用例编号【{}】,预期结果关键字key：{},\n预期结果：{},\n实际结果：{}".format(case_id, expect_key,expect_result, res))




if __name__ == '__main__':
    unittest.main()
