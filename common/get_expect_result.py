#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import operator
from deepdiff import DeepDiff
from utils.config import ParserConfig
from utils.operate_json import Operate_Json

expect_result_Path = os.path.join(ParserConfig().get_path(), 'data','expect_result.json')


class Get_Expect_Result():

    def __init__(self):
        self.json = Operate_Json(expect_result_Path)
        self.data = self.read_result()


    #读取result文件
    def read_result(self):
        data = self.json.read_data()
        return data


    #根据关键字获取预期结果json数据,将列表数据转换为字典数据
    def get_key_result(self,key=None):
        try:
            data = self.json.get_data(key)
            if type(data)==list:
                new_data = {k: v for i in data for (k, v) in i.items()}
                return new_data
            elif  type(data)==dict:
                return data
        except KeyError as err:
            print('关键字key没有匹配到预期结果:\n{0}'.format(err))


    #获取预期结果--文本信息
    def get_result_desc(self,url_key,desc):
        data = self.json.get_data(url_key)
        if data != None:
            for i in data:
                message = i.get(desc)
                if message:
                    return message
        return None



    #获取预期结果--json数据
    def get_result_json(self,url_key,status):
        data = self.json.get_data(url_key)
        if data != None:
            for i in data:
                message = i.get(status)
                if message:
                    return message
        return None



    #判断两个字典是否相等
    def assert_result_dict(self,dict1, dict2):
        if isinstance(dict1, dict) and isinstance(dict2, dict):
            cmp_dict = DeepDiff(dict1, dict2, ignore_order=True).to_dict()
            if cmp_dict.get("dictionary_item_added"):
                return False
            else:
                return True
        return False




    #判断一个字符串是否包含在另外一个字符串
    def is_contain(self,str_one,str_two):
        flag = None
        if operator.contains(str_one,str_two):
            flag = True
        else:
            flag = False
        return flag




if __name__ == "__main__":

    dict1 = {"aaa": "AAA", "ccc": "BBBB", "bbb": "A1A", "CC": [{"11": "22"}, {"11": "44222"}]}
    dict2 = {"aaa": "AAA", "ccc": "BBBB", "bbb": "A1A", "CC": [{"11": "22"}, {"11": "44666"},{"1ttt": "44666"}],"ddd":"44tg"}

    op_result = Get_Expect_Result()
    data = op_result.get_key_result('品牌分页')
    print(data)
    print(type(data))



