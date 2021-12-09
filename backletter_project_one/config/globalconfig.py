#coding=utf-8
import os
from backletter_project_one.utils.ReadConfigIni import ReadConfigIni

# 获取config.ini的路径
file_path = os.path.split(os.path.realpath(__file__))[0] #分开文件名和路径，取其中的路径
# print(file_path)  #C:\python-3.7.3-amd64\backletter_project_one\config

#读取配置文件
read_config = ReadConfigIni(os.path.join(file_path,"config.ini"))
# print(read_config)

# 获取项目路径的第一种方法
project_path = read_config.getConfigValue("project","project_path")
# print(project_path)

# 获取项目路径的第二种方法
project_path = os.path.dirname(os.path.dirname(__file__))
# print(project_path)  #C:/python-3.7.3-amd64/backletter_project_one

# 测试用例路径
TestCase_path = os.path.join(project_path,"Test_case")
# print(TestCase_path)

# 测试报告路径
report_path = os.path.join(project_path,"report","html","2021-11-22")
# print(report_path)Test

# 测试数据路径
data_path = os.path.join(project_path,"Test_manage")
# print(data_path)

#config.ini路径
ini_path = os.path.join(project_path,"config")
# print(ini_path)







