#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import unittest

from utils.operate_excel import Operate_Excel
from utils.operate_json import Operate_Json
from utils.config import ParserConfig
from common.get_expect_result import Get_Expect_Result


Testcase_Path = os.path.join(ParserConfig().get_path(), 'data','Testcase.xlsx')
expect_result_Path = os.path.join(ParserConfig().get_path(), 'data','expect_result.json')

class Assert_Result():

    def __init__(self):
        self.op_excel = Operate_Excel()
        self.op_parser = ParserConfig()
        self.get_expect_result = Get_Expect_Result()
        self.op_json = Operate_Json(file_path=expect_result_Path)

    def assert_result(self,response,mode):

        #获取响应状态码
        if mode == 'code':
            col = self.op_parser.get_expect_result()
            expect_result = self.op_excel.get_cell_value(row,col)
            actual_result = response['code']
            if int(expect_result) == int(actual_result):
                print('通过，\n预期结果:{0} \n实际结果:{1}'.format(expect_result,actual_result))
            else:
                print('失败，\n预期结果:{0} \n实际结果:{1}'.format(expect_result,actual_result))


        elif mode == 'desc':
            expect_result = self.get_expect_result.get_result_desc()
            actual_result = response['desc']



        elif mode == 'json':

        elif mode == 'dict':



















if __name__ == "__main__":
    data = {"code":200,"success":"true","data":{"id":"1453332101518143489","createUser":"1446292876069801986","createDept":"1446315795123077121","createTime":"2021-10-27 20:05:49","updateUser":"1446292876069801986","updateTime":"2021-10-27 20:05:49","status":1,"isDeleted":0,"firmCode":"TMQC","firmName":"天美汽车","brandId":"1453312112522244097","brandCode":"","brandName":""},"msg":"操作成功"}
    ar = Assert_Result()
    data2 = ar.assert_result(response=data ,mode='code',row=5)
    print(data2)
