# -*- coding:utf-8 -*-
# @Time : 2021/12/2 14:22
# @Author : ASUS
# @File : test_register.py


import unittest
from backletter_project_one.config.base_page import *
from backletter_project_one.config.Page_Element import Page_Element as p

class Test_register(unittest.TestCase):

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

    #注册账号
    def test_register(self):

        sleep(3)
        #点击用户注册
        self.base.click(self.base.find_element(p.zc_register))
        sleep(3)
        #输入手机号
        self.base.send_keys(self.base.find_element(p.zc_mobile_number),zc_mobile_numbe)
        sleep(3)
        #输入图形验证码
        self.base.send_keys(self.base.find_element(p.zc_picture_code),zc_picture_code)
        sleep(3)
        #点击获取短信验证码
        self.base.click(self.base.find_element(p.zc_verify))
        sleep(3)
        try:
            self.assertEqual(self.base.find_element(p.zc_prompt_message).text,'手机号已注册，请直接登录')
            self.base.click(self.base.find_element(p.zc_denglu))
            # self.tearDown()

        except AssertionError as e:
            self.zc=str(e)
            self.log.add_log('执行结果:' ,self.zc ,'执行失败')

        try:
            self.assertEqual(self.base.find_element(p.zc_verify_code).text, '验证码不正确')
            # 输入短信验证码
            self.base.send_keys(self.base.find_element(p.zc_message_code), zc_message_code)
            sleep(3)
            # 输入登录密码
            self.base.send_keys(self.base.find_element(p.zc_passwordone), zc_passwordone)
            sleep(3)
            # 输入确认登录密码
            self.base.send_keys(self.base.find_element(p.zc_passwordtwo), zc_passwordtwo)
            sleep(3)
            # 点击立即注册
            self.base.click(self.base.find_element(p.zc_button))
            sleep(6)
            self.base.test_Screenshot()

        except AssertionError as e:
                self.zc = str(e)
                self.log.add_log('执行结果:', self.zc, '执行失败')




if __name__ == '__main__':
    unittest.main()