import json

from utils.config import ParserConfig
from utils.operate_header import Operate_Header
from utils.operate_excel import Operate_Excel
from utils.operate_json import Operate_Json
from common.http_request import Request_Method
from utils.log import Logger


class Login_info():

	def __init__(self):
		self.excel = Operate_Excel()
		self.parser = ParserConfig()
		self.json = Operate_Json()
		self.header = Operate_Header()
		self.run = Request_Method()

	def login(self):
		host = self.parser.get_url_parameter()
		url = host + "api/blade-auth/oauth/token?"
		method = 'post'
		header_login = self.header.get_header_data_key('login')
		data = {
			"username": self.parser.get_section_options('server', 'username'),
			"password": self.parser.get_section_options('server', 'password'),
			"tenantId": self.parser.get_section_options('server', 'tenantId'),
			"grant_type": self.parser.get_section_options('server', 'grant_type'),
			"scope": self.parser.get_section_options('server', 'scope'),
			"type": self.parser.get_section_options('server', 'type')
		}

		response = self.run.run_main(url=url,method=method,data=data,headers=header_login)
		res = json.loads(response)
		print("登录成功，响应信息:", type(res), res)

		# 将响应信息更新到请求头header
		Content_Type_form = self.header.Content_Type_form(res)
		Content_Type_json = self.header.Content_Type_json(res)
		# 将响应信息更新到请求头header
		headers = self.header.get_header_data()
		# 更新header配置文件数据件
		headers["Content_Type_form"] = Content_Type_form
		headers["Content_Type_json"] = Content_Type_json
		# 将新请求头headers,保存至配置文件
		self.header.write_header_data(headers)


		"----------------分割线-------------------------"
		# 获取门店信息
		url2 = host + "api/blade-system/dept/userDeptList"
		data2 = {"dept_info": ""}
		header2 = self.header.get_header_data_key('Content_Type_form')
		response2 = self.run.run_main(method='get', url=url2, data=data2, headers=header2)
		res2 = json.loads(response2)
		Update_Content_Type_form = self.header.Update_Content_Type_form(res2)
		Update_Content_Type_json = self.header.Update_Content_Type_json(res2)
		# 将响应信息更新到请求头header
		headers = self.header.get_header_data()
		# 更新header配置文件数据件
		headers["Content_Type_form"] = Update_Content_Type_form
		headers["Content_Type_json"] = Update_Content_Type_json
		# 将新请求头headers,保存至配置文件
		self.header.write_header_data(headers)



if __name__ == '__main__':
	login = Login_info()
	data = login.login()
	print(data)


