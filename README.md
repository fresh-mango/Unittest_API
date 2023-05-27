# Unittest_API
Python+unittest+HTMLTestRunner数据驱动接口自动化测试框架,共七个大模块，详细信息如下说明。





common：

--assert_result.py：自定义断言，在断言的时候可以调入该类

--dependent_data.py：运行依赖接口，获取依赖测试用例数据

--get_excel_data.py：获取excel文档上的数据

--get_expect_result.py：获取预期结果数据

--HTMLTestRunner.py：这个是HTMLTestRunner源文件

--http_request.py：这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应



config:

--caselist.txt:配置将要执行testCase目录下的哪些用例文件，前加#代表不进行执行。当项目过于庞大，用例足够多的时候，我们可以通过这个开关，来确定本次执行哪些接口的哪些用例。

--config.ini：数据库、邮箱、接口、日志等的配置项，用于方便的调用读取

--header.json：请求头信息



data:

--expected_result.json:预期结果数据

--request_data.json：请求数据信息

--Testcase.xlsx：测试用例case



result:

--log:生成的日志文件

--report:生成的测试报告



run_main:

--run_suite.py:主程序入口，开始执行接口自动化，项目工程部署完毕后直接运行该文件即可



testcase:

--test_case.py:常规test_case模板,case维护在程序代码中

--test_case_ddt.py:ddt模板，case参数化方式为ddt

--test_case_dependent.py:依赖接口模板，主要是处理依赖接口逻辑关系

--test_case_parameterized.py：parameterized模板，case参数化方式为parameterized

--test_login.py：登录case,登录成功后将请求头信息存储至配置文件



utils:

--config.py:读取配置文件的方法，并返回文件中内容

--connect_db.py:这个文件是数据库连接池的相关内容

--dateencoder_json.py:数据转码，在连接数据库时需要调入该类

--e_mail.py：这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑

--log.py：调用该类的方法，用来打印生成日志

--operate_excel.py：封装读取Excel的方法

--operate_header.py：封装请求头信息

--operate_json.py：封装读取json的方法

