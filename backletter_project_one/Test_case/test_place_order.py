# -*- coding:utf-8 -*-
# @Time : 2021/12/2 9:11
# @Author : ASUS
# @File : test_place_order.py

import unittest
from backletter_project_one.config.base_page import *
from backletter_project_one.config.Page_Element import Page_Element as p


class Test_place_order(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("类的开始")
    @classmethod
    def tearDownClass(cls):
        print("类的结束")

    def setUp(self):
        self.base = Base_page()
        self.base.start_window()
        self.log = Log()

    def tearDown(self):
        self.base.quit_window()

    # 订购标段
    def test_place_order(self):

        sleep(3)
        #输入手机号
        self.base.send_keys(self.base.find_element(p.mobile_number),zc_mobile_numbe)
        sleep(3)
        #输入登录密码
        self.base.send_keys(self.base.find_element(p.password),zc_passwordone)
        sleep(3)
        #点击立即登录
        self.base.click(self.base.find_element(p.log_in))
        sleep(3)

        #搜索项目
        self.base.send_keys(self.base.find_element(p.Search_project),project)
        sleep(3)
        #点击搜索
        self.base.click(self.base.find_element(p.Click_inquire_one))
        sleep(3)
        #点击查看项目
        self.base.click(self.base.find_element(p.Check_project))
        sleep(3)

        # 搜索标段
        self.base.send_keys(self.base.find_element(p.Search_blocks), blocks)
        sleep(3)
        # 点击查询
        self.base.click(self.base.find_element(p.Click_inquire_two))
        sleep(3)
        #点击申请标段
        self.base.click(self.base.find_element(p.Application_blocks))
        sleep(3)
        self.base.roll_window_two()
        sleep(3)
        #点击确定进入下一步
        self.base.click(self.base.find_element(p.Next_step))
        sleep(30)


if __name__ == '__main__':
    unittest.main()