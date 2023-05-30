#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import json

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
REQUEST_DATA_PATH = os.path.join(BASE_PATH, 'data','request_data.json')

class Operate_Json():
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path = REQUEST_DATA_PATH
        else:
            self.file_path = file_path
        self.data = self.read_data()

    #读取json文件
    def read_data(self):
        with open(self.file_path,encoding='utf-8-sig',errors='ignore') as fp:
            data= json.load(fp,strict=False)
            #data = fp.readline()
            return data

    #根据关键字获取数据
    def get_data(self,key=None):
        try:
            if key:
                return self.data[key]
            else:
                return None
        except KeyError as err:
            print('关键字key没有匹配到数据:\n{0}'.format(err))

    #写json数据
    def write_data(self,data):
        with open(file_path,'w') as fp:
            fp.write(json.dumps(data)+'\n')





if __name__ == "__main__":
    opjson = Operate_Json()
    data = opjson.get_data("add_brand")
    print(type(data),data)


