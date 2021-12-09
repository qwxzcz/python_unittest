# -*- coding:utf-8 -*-
# @Time : 2021/12/6 17:00
# @Author : ASUS
# @File : test_issue_invoice.py

import unittest
from backletter_project_one.config.base_page import *
from backletter_project_one.config.Page_Element import Page_Element as p

class Test_apply_invoice(unittest.TestCase):

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

    def test_apply_invoice(self):

        # 下载保函
        # self.base.click(self.base.find_element(p.download_backletter))
        sleep(3)
        self.base.roll_window_two()
        sleep(3)
        # 点击申请发票
        self.base.click(self.base.find_element(p.apply_invoice))
        sleep(3)

        # # 申请电子发票
        # self.base.click(self.base.find_element(p.electronic_invoice))
        # sleep(3)
        # # 输入电子发票地址(非纸质)
        # self.base.send_keys(self.base.find_element(p.email), email)
        # sleep(3)
        # # 点击提交
        # self.base.click(self.base.find_element(p.submit_one))
        # sleep(6)
        # self.base.test_Screenshot()
        # 下载电子发票
        # self.base.click(self.base.find_element())


        # 申请普通发票(纸质)
        self.base.click(self.base.find_element(p.regular_invoice))
        sleep(3)
        # 输入收件人
        self.base.send_keys(self.base.find_element(p.recipients), recipients)
        sleep(3)
        # 输入收件人手机号
        self.base.send_keys(self.base.find_element(p.recipients_mobile), recipients_mobile)
        sleep(3)
        # 输入收件地址
        self.base.send_keys(self.base.find_element(p.consignee_address), consignee_address)
        sleep(3)
        # 输入注册地址
        self.base.send_keys(self.base.find_element(p.registered_address), registered_address)
        sleep(3)
        # 输入联系电话
        self.base.send_keys(self.base.find_element(p.contact_number), contact_number)
        sleep(3)
        # 输入开户行
        self.base.send_keys(self.base.find_element(p.opening_bank), opening_bank)
        sleep(3)
        # 输入开户账号
        self.base.send_keys(self.base.find_element(p.account_number), account_number)
        sleep(3)
        # 点击提交
        self.base.click(self.base.find_element(p.submit_two))
        sleep(6)
        # 查看收件人信息
        self.base.click(self.base.find_element(p.check_recipients_information))
        sleep(3)
        self.base.test_Screenshot()


if __name__ == '__main__':
    unittest.main()