# Api-automated-scripts
---
用于api测试，项目整体架构如下
---

common：

——configDb.py：这个文件主要编写数据库连接池的相关内容，方便使用。

——configEmail.py：这个文件主要是配置发送邮件的主题、正文等，将测试报告发送并抄送到相关人邮箱的逻辑。

——configHttp.py：这个文件主要来通过get、post、put、delete等方法来进行http请求，并拿到请求响应。

——HTMLTestRunner.py：主要是生成测试报告相关

——Log.py：调用该类的方法，用来打印生成日志

Config :

——case.yaml : yaml格式存储的测试用例

——code_message.json : 该文件主要存放接口各个状态码和错误码，更方便回归的校验

——cookie.json : 该文件主要存储cookie

——header.json : 该文件用于存储request的请求头数据以及token等数据，用于其他接口调用

——result.json: 存储部分接口响应数据，用于回归时的数据全量校验

result :

——logs：生成的日志文件

——report.html：生成的测试报告

testCase :

——test01case.py：读取userCase.xlsx中的用例，使用unittest来进行断言校验

testFile/case :

——userCase.xlsx：Excel格式存放测试用例

——allPairs_data.xlsx : 存放通过正交法生成的测试数据

Until ：

——codition_data.py : 上下游接口依赖参数传递的封装

——CryDEC.py : 根据项目的加密规则封装的加解密函数

——geturlParams.py：获取接口的URL、参数、method等

——handle_json.py : 读取对应的json文件

——handle_result.py : 读取存放响应数据的json文件

——readConfig.py：读取配置文件的方法，并返回文件中内容

——readExcel.py：读取Excel的方法

caselist.txt：配置将要执行testCase目录下的哪些用例文件，前加#代表不进行执行。当项目过于庞大，用例足够多的时候，我们可以通过这个开关，来确定本次执行哪些接口的哪些用例。

config.ini：数据库、邮箱、测试和uat环境等的配置项，用于方便的调用读取。

getpathInfo.py：获取项目绝对路径

runAll.py：开始执行接口自动化，项目工程部署完毕后直接运行该文件即可

test_api.py：使用flask提供本地测试的接口服务

exsice_assert : 
             部分复杂业务脚本化，同样用于创造测试数据

——————
基础架构思路来源于博主「songlh1234」
