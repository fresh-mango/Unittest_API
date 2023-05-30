#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
import unittest
import HTMLTestRunner
from utils.config import report_path,testcase_path,caselist_path
from utils.e_mail import Email
from utils.log import Logger


class Run_Suite():

    def __init__(self):
        self.caselist = []
        self.log = Logger().get_logger()

    def get_caselist(self):
        with open(caselist_path,'r') as fp:
            for line in fp.readlines():
                data = str(line)
                if data != '' and not data.startswith("#"):
                    self.caselist.append(data.replace("\n", ""))
        return  self.caselist

    def set_case_suite(self):
        test_suite = unittest.TestSuite()
        suite_module = []
        for case in  self.get_caselist():
            case_name = case.split("/")[-1]  # 通过split函数来将aaa/bbb分割字符串，-1取后面，0取前面
            discover = unittest.defaultTestLoader.discover(testcase_path,pattern = case_name + '.py',top_level_dir=None)
            suite_module.append(discover)#将discover存入suite_module元素组


        if len(suite_module) > 0:#判断suite_module元素组是否存在元素
            for suite in suite_module:#如果存在，循环取出元素组内容，命名为suite
                for case_name in suite:#从discover中取出case_name，使用addTest添加到测试集
                    test_suite.addTest(case_name)
        else:
            return None
        return test_suite#返回测试集



    def run_case_suite(self):
        try:
            suit = self.set_case_suite()#调用set_case_suite获取test_suite
            print(str(suit))
            if suit is not None:#判断test_suite是否为空
                now = time.strftime("%Y-%m-%d-%H %M %S", time.localtime(time.time()))
                filename = report_path + "\\" + now + "-" + "ResultReport.html"
                with open(filename, 'wb') as fp:
                    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"测试报告",
                                                           description=u"测试用例执行的结果", verbosity=2)
                    runner.run(suit)


            else:
                print("没有要执行的测试用例.")
        except Exception as ex:
            print(str(ex))
            self.log.info(str(ex))


        finally:
            print("*********TEST END*********")
            self.log.info(str("*********TEST END*********"))

        e = Email()
        e.send_email()




if __name__ == "__main__":
    c = Run_Suite()
    data = c.run_case_suite()
