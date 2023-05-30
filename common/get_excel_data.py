#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from utils.config import ParserConfig
from utils.operate_json import Operate_Json
from  utils.operate_excel import Operate_Excel

class Get_Excel_Data():
    def __init__(self):
        self.excel = Operate_Excel()
        self.parser = ParserConfig()
        self.json = Operate_Json()


    #获取前置（依赖）case与被依赖case,将数据转换为字典类型
    def get_dependent_cases(self):
        list_dict = {}
        rows = self.excel.get_rows()
        for row in range(rows)[1:]:
            depend_case = self.get_depend_case(row)
            case_id = self.get_case_id(row)
            if depend_case != None:
                list_dict[depend_case]=case_id

        return list_dict

    # 获取前置（依赖）case与被依赖case,将数据转换为列表类型
    def get_dependent_cases_list(self):
        case_list = []
        case_lists = self.get_dependent_cases()
        for k, v in case_lists.items():
            data = (f'{k}:{v}')
            case_list.append(data)
        return case_list


    #获取常规测试用例
    def get_general_case(self):
        case_list = self.excel.test_case_list_yes()
        return case_list

    #获取excel行数，暨case个数
    def get_case_lines(self):
        return self.excel.get_rows()





    #获取case_id
    def get_case_id(self,row):
        col = self.parser.get_case_id()
        case_id = self.excel.get_cell_value(row,col)
        if case_id == "":
            return None
        else:
            return case_id

    #判断是否执行
    def get_is_run(self,row):
        flag = None
        col = self.parser.get_is_run()
        run_model = self.excel.get_cell_value(row,col)
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag


    #判断前置条件是否有case依赖
    def get_depend_case(self,row):
        col = self.parser.get_pre_condition()
        depend_case_id = self.excel.get_cell_value(row,col)
        if depend_case_id == "":
            return None
        else:
            return depend_case_id




    #获取依赖数据的key
    def get_depend_key(self,row):
        col = self.parser.get_data_depend()
        depend_key = self.excel.get_cell_value(row-1,col)
        if depend_key == "":
            return None
        else:
            return depend_key






    #获取数据依赖字段
    def get_depend_field(self,row):
        col =self.parser.get_field_depend()
        field_data = self.excel.get_cell_value(row-1,col)
        if field_data == "":
            return None
        else:
            return field_data


    #获取url
    def get_request_url(self,row):
        col = self.parser.get_url()
        url =self.excel.get_cell_value(row,col)
        return url


    #获取请求方式
    def get_request_method(self,row):
        col = self.parser.get_request_method()
        request_method = self.excel.get_cell_value(row,col)
        return request_method


    #获取请求头内容格式
    def get_header_format(self,row):
        col = self.parser.get_format_type()
        format_type = self.excel.get_cell_value(row,col)
        return format_type


    #获取请求数据的关键字key
    def get_request_key(self,row):
        col =self.parser.get_request_data()
        request_key = self.excel.get_cell_value(row,col)
        if request_key == "":
            return None
        else:
            return  request_key


    #通过获取关键字key拿到请求数据
    def get_data_for_json(self,row):
        request_data = self.json.get_data(self.get_request_key(row))
        return request_data


    #是否写入cookie
    def get_operate_cookie(self,row):
        col =self.parser.get_op_cookie()
        operate_cookie = self.excel.get_cell_value(row,col)
        if operate_cookie != "":
            return operate_cookie
        else:
            return None


    #是否携带header
    def get_operate_header(self,row):
        col = self.parser.get_op_header()
        operate_header = self.excel.get_cell_value(row,col)
        if operate_header != "":
            return operate_header
        else:
            return None


    #获取预期结果
    def get_expect_result(self,row):
        col =self.parser.get_expect_result()
        expect_result = self.excel.get_cell_value(row,col)
        if expect_result == "":
            return None
        else:
            return expect_result



    #写日志数据
    def write_result(self,row,value):
        col =self.parser.get_daily_data()
        self.excel.excel_write_data(row,col,value)







if __name__ == "__main__":
    op = Get_Excel_Data()
    data = op.get_general_case()
    print(data)

