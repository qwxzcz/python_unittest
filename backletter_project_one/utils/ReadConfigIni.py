#coding=UTF-8
import configparser
import os

'''
configparser这个模块用来读取ini文件
'''

class ReadConfigIni(object):
    """
    实例化configparser
    """
    def __init__(self,filename):
        self.cf = configparser.ConfigParser()   #创建对象self.cf
        self.cf.read(filename)

    # 读ini文件的操作
    def getConfigValue(self,section, option):
        value = self.cf.get(section, option)
        return value


# # 验证ReadConfigIni是否可以读取ini文件
# project_path = os.path.dirname(os.path.dirname(__file__))#获取当前目录的绝对路径
# # print(project_path)
# path = os.path.join(project_path,"config",'config.ini')
# # print (path)  #C:/python-3.7.3-amd64/backletter_project_one\config\config.ini
# read_config = ReadConfigIni(path)
# #
# # #获取config.ini中的 test_data的数据
# mobile_number= read_config.getConfigValue("test_data","mobile_number")
# # print(mobile_number)
# password= read_config.getConfigValue("test_data","password")
# # print(password)






