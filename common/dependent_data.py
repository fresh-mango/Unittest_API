#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from utils.operate_json import Operate_Json
from utils.config import ParserConfig
from common.http_request import Request_Method
from utils.operate_header import Operate_Header
from common.get_excel_data import Get_Excel_Data
from jsonpath_rw import jsonpath,parse
from utils.operate_excel import Operate_Excel


class Dependent_Data():

    def __init__(self,case_id):
        self.case_id = case_id
        self.excel = Operate_Excel()
        self.json = Operate_Json()
        self.parser = ParserConfig()
        self.run = Request_Method()
        self.header_info = Operate_Header()
        self.excel_data = Get_Excel_Data()



    # 通过case_id去获取该case_id的整行数据
    def get_case_line_data(self):
        row_num = self.excel.get_rows_number(self.case_id)
        row_data = self.excel.get_rows_value(row_num)
        return row_data

    #执行前置条件所依赖的case,获取结果集
    def run_dependent(self):
        old_row_num = self.excel.get_rows_number(self.case_id)
        if old_row_num:
            row_num = old_row_num - 1
            header_form = self.header_info.get_header_data_key("Content_Type_form")
            header_json = self.header_info.get_header_data_key("Content_Type_json")
            header_format = self.excel_data.get_header_format(row_num)
            header = header_json if header_format != 'form' else header_form
            request_data = self.excel_data.get_data_for_json(row_num)
            method = self.excel_data.get_request_method(row_num)
            base_url = self.parser.get_url_parameter()
            api_url = self.excel_data.get_request_url(row_num)
            url = base_url + api_url
            res = self.run.run_main(url=url, method=method, data=request_data, headers=header)

            return json.loads(res)



    #根据依赖数据key，在前置条件所依赖的case结果集里匹配响应值，并返回响应值
    def get_data_for_key(self,row):
        try:
            depend_data = self.excel_data.get_depend_key(row)
            response_data = self.run_dependent()
            json_exe = parse(depend_data)
            madle = json_exe.find(response_data)
            return [math.value for math in madle][0]

        except IndexError  as err:
            print('依赖case运行后没有匹配到关键字:\n{0}'.format(err))
        except KeyError as err:
            print('依赖case运行后没有匹配到关键字:\n{0}'.format(err))
        except TypeError as err:
            print('依赖case运行后没有匹配到关键字:\n{0}'.format(err))




if __name__ == "__main__":
    op = Dependent_Data('USA-brand-0009')
    data = op.get_data_for_key(11)

    print(type(data),data)





