# -*- coding:utf-8 -*-
# @Time : 2021/11/24 10:39
# @Author : ASUS
# @File : base_page.py

import logging
from selenium import webdriver
#日志文件
class Log():
    def __init__(self):
        logging.basicConfig(
            level = logging.INFO,
            # log格式
            format = '%(asctime)s %(levelname)s [%(funcName)s: %(filename)s,%(lineno)d] %(message)s',
            datefmt= '%Y-%m-%d %H:%M:%S', #日期格式
            filename= './../report/log/2021-11-22/log.txt',  #日志输出文件
            filemode = 'w'  #追加模式
        )

    def add_log(self,page,func,des):
        out_str = page + ':' +func + ':' +des
        logging.info(out_str)


class Base_page():
    #浏览器初始化
    def start_window(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    #进入网址
    def enter_window(self):
        self.driver.get('http://ybdzbh.ztb.rdtest.cn/#/tenderDetail?orderNo=testZL00003627')

    #执行完成退出
    def quit_window(self):
        self.driver.quit()

    #进入最新的页面
    def to_last_window(self):
        self.driver = webdriver.Chrome()
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])



