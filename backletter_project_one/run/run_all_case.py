# @Time : 2021/11/22 11:28
# @Author : ASUS
# @File : run_all_case.py


import unittest
from backletter_project_one.utils.HTMLTestRunner3_New import HTMLTestRunner
from time import *
# from backletter_project_one.utils.mail import SendMail


Test_path= r"C:\python-3.7.3-amd64\backletter_project_one\Test_case" #测试用例路径
report_path= r"C:\python-3.7.3-amd64\backletter_project_one\report\html\2021-11-22"  #测试报告路径

now = strftime('%y-%m-%d %H-%M-%S')  # 设置当前时间
filename = report_path + "\\" + now +'_report.html' #拼接出测试报告名

def auto_run():

    d = unittest.defaultTestLoader.discover(start_dir=Test_path, pattern='test_total.py')
    fp = open(filename,"wb")
    runner = HTMLTestRunner(stream=fp, title="UI自动化测试报告", description="用例执行情况" ,tester="zcz")
    runner.run(d)

#定义一个发邮件的方法
# def send_mail():
#     sm = SendMail(send_msg=filename,attachment=filename)
#     sm.send_mail()  #创建一个对象调用SendMail类中的send_mail方法进行邮件的发送

if __name__ == '__main__':
    auto_run()

