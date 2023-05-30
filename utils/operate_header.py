#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import json
# from config import *
from utils.operate_json import Operate_Json

BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
HEADER_FILE = os.path.join(BASE_PATH, 'config','header.json')

# headers ="""
# "Accept": "application/json, text/plain, */*",
# "Accept-Encoding": "gzip, deflate",
# "Accept-Language": "zh-CN,zh;q=0.9",
# "Authorization": "Basic c2FiZXI6c2FiZXJfc2VjcmV0",
# "Captcha-Code": "7xe3u",
# "Captcha-Key": "0d3601099a7bf6a20aeae0a81e03ddab",
# "Content-Length": "0",
# "Content-Type": "application/json;charset=UTF-8",
# "dept_id": "1450296120781672450",
# "Host": "112.74.178.203:9998",
# "Origin": "http://112.74.178.203:9998",
# "Proxy-Connection": "keep-alive",
# "Referer": "http://112.74.178.203:9998/",
# "Tenant-Id": "461031",
# "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
# "Blade-Auth":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI0NjEwMzEiLCJ1c2VyX25hbWUiOiJhZG1pbiIsInJlYWxfbmFtZSI6Iua1i-ivlemmluW4rSIsImF2YXRhciI6IiIsImF1dGhvcml0aWVzIjpbImFkbWluIl0sImNsaWVudF9pZCI6InNhYmVyIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJsaWNlbnNlIjoicG93ZXJlZCBieSBibGFkZXgiLCJwb3N0X2lkIjoiMTQ0NjI5Mzk4MTc1NTkzMjY3NCIsInVzZXJfaWQiOiIxNDQ2MjkzOTk1ODQ0MTEyMzg2Iiwicm9sZV9pZCI6IjE0NDYyOTM5NzIwNDE5MjQ2MDkiLCJzY29wZSI6WyJhbGwiXSwibmlja19uYW1lIjoiYWRtaW4iLCJvYXV0aF9pZCI6IiIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sImV4cCI6MTYzNTI1MjI2NywiZGVwdF9pZCI6IjE0NDYyOTM5ODE3MjIzNzgyNDIiLCJqdGkiOiI3NjVkYTA2Ny02NTgzLTQ4M2EtOGNhZC02ODNkYzljYWI1YjkiLCJhY2NvdW50IjoiYWRtaW4ifQ.Abo2HTsgmXj3aawxbG-L3Lk5-1T6B-Nht4-JDbv0ECU",
# "Cookie":"saber-access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI0NjEwMzEiLCJ1c2VyX25hbWUiOiJhZG1pbiIsInJlYWxfbmFtZSI6Iua1i-ivlemmluW4rSIsImF2YXRhciI6IiIsImF1dGhvcml0aWVzIjpbImFkbWluIl0sImNsaWVudF9pZCI6InNhYmVyIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJsaWNlbnNlIjoicG93ZXJlZCBieSBibGFkZXgiLCJwb3N0X2lkIjoiMTQ0NjI5Mzk4MTc1NTkzMjY3NCIsInVzZXJfaWQiOiIxNDQ2MjkzOTk1ODQ0MTEyMzg2Iiwicm9sZV9pZCI6IjE0NDYyOTM5NzIwNDE5MjQ2MDkiLCJzY29wZSI6WyJhbGwiXSwibmlja19uYW1lIjoiYWRtaW4iLCJvYXV0aF9pZCI6IiIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sImV4cCI6MTYzNTI1MjI2NywiZGVwdF9pZCI6IjE0NDYyOTM5ODE3MjIzNzgyNDIiLCJqdGkiOiI3NjVkYTA2Ny02NTgzLTQ4M2EtOGNhZC02ODNkYzljYWI1YjkiLCJhY2NvdW50IjoiYWRtaW4ifQ.Abo2HTsgmXj3aawxbG-L3Lk5-1T6B-Nht4-JDbv0ECU; saber-refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0ZW5hbnRfaWQiOiI0NjEwMzEiLCJ1c2VyX25hbWUiOiJhZG1pbiIsInJlYWxfbmFtZSI6Iua1i-ivlemmluW4rSIsImF2YXRhciI6IiIsImF1dGhvcml0aWVzIjpbImFkbWluIl0sImNsaWVudF9pZCI6InNhYmVyIiwicm9sZV9uYW1lIjoiYWRtaW4iLCJsaWNlbnNlIjoicG93ZXJlZCBieSBibGFkZXgiLCJwb3N0X2lkIjoiMTQ0NjI5Mzk4MTc1NTkzMjY3NCIsInVzZXJfaWQiOiIxNDQ2MjkzOTk1ODQ0MTEyMzg2Iiwicm9sZV9pZCI6IjE0NDYyOTM5NzIwNDE5MjQ2MDkiLCJzY29wZSI6WyJhbGwiXSwibmlja19uYW1lIjoiYWRtaW4iLCJhdGkiOiI3NjVkYTA2Ny02NTgzLTQ4M2EtOGNhZC02ODNkYzljYWI1YjkiLCJvYXV0aF9pZCI6IiIsImRldGFpbCI6eyJ0eXBlIjoid2ViIn0sImV4cCI6MTYzNTgxNzQ2MiwiZGVwdF9pZCI6IjE0NDYyOTM5ODE3MjIzNzgyNDIiLCJqdGkiOiJhNGNjOGM3ZC0yMDkxLTQ3MWQtOGViNy1jYjJmMDcyY2VmNmYiLCJhY2NvdW50IjoiYWRtaW4ifQ.I4IpJOqK6zCQ96nzI9BcD4xpecO77hbHCzSJY3x3U-Y"
#
# """
#


class Operate_Header():
    def __init__(self,file_path=None):
        if file_path==None:
            self.file_path = HEADER_FILE
        else:
            self.file_path = file_path
        self.header = Operate_Json(file_path=HEADER_FILE)

    #通过配置文件获取header数据
    def get_header_data(self):
        data = self.header.read_data()
        return data

    # 通过key获取配置文件里的header数据
    def get_header_data_key(self,key=None):
        data = self.header.read_data()
        if key =='login':
            return data['login']
        elif key =='Content_Type_form':
            return data['Content_Type_form']
        elif key == 'Content_Type_json':
            return data['Content_Type_json']


     # 将header数据写到配置文件header_json里
    def write_header_data(self, data=None):
        with open(HEADER_FILE, 'w') as fp:
            fp.write(json.dumps(data) + '\n')



    #获取请求响应信息后,将相关信息赋值更新给请求头header
    def Content_Type_form(self,res):
        try:
            Content_Type_form = {}
            Content_Type_form["Content-Type"] = "application/x-www-form-urlencoded"
            Content_Type_form["Authorization"] = "Basic c2FiZXI6bGRAMTIzNDU2"
            Content_Type_form["Blade-Auth"] = "bearer " + res.get("access_token")
            Content_Type_form["Cookie"] = "saber-access-token=" + res.get("refresh_token")
            Content_Type_form["dept_id"] = res.get("dept_id")
            Content_Type_form["Tenant-Id"] = res.get("tenant_id")

            return Content_Type_form

        except TypeError as err:
            print('没有匹配到key健:\n{0}'.format(err))

    #获取请求响应信息后,将相关信息赋值更新给请求头header
    def Content_Type_json(self,res):
        try:
            Content_Type_json = {}
            Content_Type_json["Content-Type"] = "application/json;charset=UTF-8"
            Content_Type_json["Authorization"] = "Basic c2FiZXI6bGRAMTIzNDU2"
            Content_Type_json["Blade-Auth"] = "bearer " + res.get("access_token")
            Content_Type_json["Cookie"] = "saber-access-token=" + res.get("refresh_token")
            Content_Type_json["dept_id"] = res.get("dept_id")
            Content_Type_json["Tenant-Id"] = res.get("tenant_id")

            return Content_Type_json

        except TypeError as err:
            print('没有匹配到key健:\n{0}'.format(err))


    #更新信息_form格式请求头
    def Update_Content_Type_form(self,response=None):
        try:
            Content_Type_form = self.get_header_data_key('Content_Type_form')
            Content_Type_form["dept_id"] = response['data'][0]['id']
            return Content_Type_form

        except TypeError as err:
            print('没有匹配到key健:\n{0}'.format(err))


    #更新信息_json格式请求头
    def Update_Content_Type_json(self,response=None):
        try:
            Content_Type_json = self.get_header_data_key('Content_Type_json')
            Content_Type_json["dept_id"] = response['data'][0]['id']
            return Content_Type_json

        except TypeError as err:
            print('没有匹配到key健:\n{0}'.format(err))



    #生成header信息
    def gen_headers(self, s):
        ls = s.split('\n')
        lsl = []
        ls = ls[1:-1]
        headers = {}
        for l in ls:
            l = l.split(': ')
            lsl.append(l)
        for x in lsl:
            headers[str(x[0]).strip('    ')] = x[1]
        return headers



if __name__ == "__main__":
    oh = Operate_Header()
    data = oh.get_header_data()
    print(data)


