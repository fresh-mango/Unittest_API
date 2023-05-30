#!/usr/bin/env python
# -*- encoding: utf-8 -*-


import requests
import json


class Request_Method():
    def post_main(self,url,data,header=None):
        res=None
        if header != None:
            res = requests.post(url=url,data=data,headers=header,verify=False).json()
        else:
            res = requests.post(url=url,data=data,verify=False).json()
        return res


    def get_main(self,url,data=None,header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header,verify=False).json()
        else:
            res = requests.get(url=url, data=data,verify=False).json()
        return res


    def run_main(self,method,url,data=None,headers=None):
        res = None
        if method == 'post':
            res = self.post_main(url,data,headers)
        else:
            res = self.get_main(url,data,headers)
        return json.dumps(res,ensure_ascii=False,sort_keys=True,indent=2)


if __name__ == "__main__":
    url = "http://lduat.xsdmt.com.cn/api/blade-auth/oauth/token?"
    data = {
        "tenantId": "683252",
        "username": "admin",
        "password": "670b14728ad9902aecba32e22fa4f6bd",
        "username": "admin",
        "grant_type": "password",
        "scope": "all",
        "type": "account"

    }
    header = {"Authorization": "Basic c2FiZXI6bGRAMTIzNDU2", "Tenant-Id": "683252"}
    rm = Request_Method()

    data = rm.run_main(method='post', url=url, data=data,headers = header)
    data1 = json.loads(data)
    print(type(data1), data1)




