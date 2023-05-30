"""
项目公共内容配置，以及读取配置文件中的配置。这里配置文件用的yaml，也可用其他如XML,INI等，需在file_reader中添加相应的Reader进行处理。
"""
#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import os
import configparser

# 所有相关文件的路径

# 通过当前文件的绝对路径，其父级目录一定是框架的base目录，然后确定各层的绝对路径。如果你的结构不同，可自行修改。
# 之前直接拼接的路径，修改了一下，用现在下面这种方法，可以支持linux和windows等不同的平台，也建议大家多用os.path.split()和os.path.join()，不要直接+'\\xxx\\ss'这样
base_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
config_file = os.path.join(base_path, 'config', 'config.ini')
header_file = os.path.join(base_path, 'config', 'header.json')
request_data_path = os.path.join(base_path, 'data', 'request_data.json')
expect_result_path = os.path.join(base_path, 'data', 'expected_result.json')
driver_path = os.path.join(base_path, 'drivers')
log_path = os.path.join(base_path,'result', 'log')
report_path = os.path.join(base_path, 'result', 'report')
screenshot_path = os.path.join(base_path, 'result', 'screenshot')
suite_path = os.path.join(base_path, 'suite')
testcase_excel_path = os.path.join(base_path, 'data', 'Testcase.xlsx')
testcase_path = os.path.join(base_path, 'testcase')
caselist_path= os.path.join(base_path, 'config','caselist.txt')




class ParserConfig():
    def load_ini(self):
        config = configparser.ConfigParser()
        config.read(config_file, encoding="utf-8-sig")
        return config

    #获取顶层路径
    def get_path(self):
        base_path =os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
        return base_path

    #获取某个节点的全部配置项信息
    def get_section(self,node=None):
        if node == None:
            node = 'server'
        datas = self.load_ini()
        try:
            data = datas.options(node)
        except Exception:
            print("没有获取到配置节点信息")
            data = None
        return data

    # 获取单个节点的某项配置信息
    def get_section_options(self,node=None,key=None):
        if node == None:
            node = 'server'
            key='host'
        datas = self.load_ini()
        try:
            data = datas.get(node, key)
        except Exception:
            print("没有获取到配置节点选项信息")
            data = None
        return data


    #获取动态URL
    def get_url_parameter(self):
        scheme = self.get_section_options('server','scheme')
        baseurl = self.get_section_options('server', 'baseurl')
        port = self.get_section_options('server', 'port')
        host = scheme + '://' + baseurl  + '/'
        return host

    """------分割线-------获取[server]节点信息------"""
    #获取[server]节点--服务器IP
    def get_serverIp(self):
        return self.get_section_options('server','host')

    #获取[server]节点--用户名
    def get_username(self):
        return self.get_section_options('server','username')

    #获取[server]节点--密码
    def get_password(self):
        return self.get_section_options('server','password')

    #获取[server]节点--租户ID
    def get_tenantId(self):
        return self.get_section_options('server','tenantId')



    """------分割线-------获取[excel]节点信息------"""

    #获取[excel]节点--测试用例编号
    def get_case_id(self):
        return int(self.get_section_options('excel','case_id'))

    #获取[excel]节点--接口名
    def get_api_name(self):
        return int(self.get_section_options('excel','api_name'))

    #获取[excel]节点--测试用例名称
    def get_case_name(self):
        return int(self.get_section_options('excel','case_name'))

    #获取[excel]节点--优先级
    def get_priority(self):
        return int(self.get_section_options('excel','priority'))

    #获取[excel]节点--测试用例是否运行
    def get_is_run(self):
        return int(self.get_section_options('excel','is_run'))

    #获取前置条件
    def get_pre_condition(self):
        return int(self.get_section_options('excel','pre_condition'))

    #获取依赖数据
    def get_data_depend(self):
        return int(self.get_section_options('excel','data_depend'))

    #获取数据依赖字段
    def get_field_depend(self):
        return int(self.get_section_options('excel','field_depend'))

    #获取[excel]节点--接口请求url
    def get_url(self):
        return int(self.get_section_options('excel','url'))

    #获取[excel]节点--接口请求方法
    def get_request_method(self):
        return int(self.get_section_options('excel','request_method'))

    #获取[excel]节点--接口请求格式类型
    def get_format_type(self):
        return int(self.get_section_options('excel','format_type'))

    #获取[excel]节点--请求数据
    def get_request_data(self):
        return int(self.get_section_options('excel','request_key'))

    #获取cookie操作
    def get_op_cookie(self):
        return int(self.get_section_options('excel','operate_cookie'))

    #获取header操作
    def get_op_header(self):
        return int(self.get_section_options('excel','operate_header'))

    #获取预期结果方式
    def get_expect_method(self):
        return int(self.get_section_options('excel','expect_method'))

    #获取预期结果
    def get_expect_result(self):
        return int(self.get_section_options('excel','expect_result'))

    #获取实际结果
    def get_actual_result(self):
        return int(self.get_section_options('excel','actual_result'))

    #获取日志数据
    def get_daily_data(self):
        return int(self.get_section_options('excel','diary_data'))

    #获备注信息
    def get_remark(self):
        return int(self.get_section_options('excel','remark'))



if __name__ == "__main__":
    pc = ParserConfig()
    data = pc.get_url_parameter()
    print(type(data),data)




