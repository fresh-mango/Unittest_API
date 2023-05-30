#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
import unittest
from common.http_request import Request_Method
from utils.operate_header import Operate_Header
from utils.operate_json import Operate_Json
from utils.config import ParserConfig
from utils.log import Logger
from testcase.test_login import Login_info



class Test_Case(unittest.TestCase):

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
        self.parser = ParserConfig()
        self.loger = Logger().get_logger()




    def tearDown(self) -> None:
        pass

    def test_01(self):
        host = self.parser.get_url_parameter()
        url = host + "api/ld-uas/carbrand/submit"
        method ='post'
        print(url)
        data = {
            "brandName": "永生",
            "firstLetter": "Y",
            "brandCode": "YS",
            "countryName": "1",
            "technologyTypeName": "1",
            "logoUrl": "upload/20211112/363d77d9d25927a26d972a1b2165cd24.png",
            "country": "1",
            "technologyType": "1"
        }
        header = self.header_info.get_header_data_key('Content_Type_json')
        response = self.run.run_main(method=method, url=url, data=json.dumps(data), headers=header)
        res = json.loads(response)
        print("响应信息：{}，\n预期结果：{},\n实际结果：{}".format(res, 200, res["code"]))
        self.loger.info('请求响应信息：')
        self.loger.info(res)
        self.assertEqual(200,res["code"])



    def test_02(self):
        host = self.parser.get_url_parameter()
        url = host + "api/ld-uas/carbrand/page?"
        data =  {
            "brandCode": "YJ",
            "brandName": "",
            "firstLetter": "",
            "current": "1",
            "size": "20"
        }
        header = self.header_info.get_header_data_key('Content_Type_form')
        response = self.run.run_main(method='get', url=url, data=json.dumps(data), headers=header)
        res = json.loads(response)
        self.loger.info('请求响应信息：')
        self.loger.info(res)
        self.assertEqual(100005,res["code"])
        print("响应信息：{}，\n预期结果：{},\n实际结果：{}".format(res, 100005 , res["code"]))


    def test_03_厂商详情(self):
        host = self.parser.get_url_parameter()
        url = host + "api/ld-uas/carfirm/detail?"
        data = {"id": "1459586954372395010"}
        header = self.header_info.get_header_data_key('Content_Type_form')
        response = self.run.run_main(method='get', url=url, data=data, headers=header)
        res = json.loads(response)
        self.loger.info('请求响应信息：')
        self.loger.info(res)
        self.assertEqual(200, res["code"])
        print("响应信息：{}，\n预期结果：{},\n实际结果：{}".format(res, 200 , res["code"]))




if __name__ == '__main__':
    unittest.main()
