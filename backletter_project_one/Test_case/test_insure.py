# @Time : 2021/11/22 10:18
# @Author : ASUS
# @File : test_insure.py

import unittest
from backletter_project_one.config.base_page import *
from backletter_project_one.config.Page_Element import Page_Element as p

class Test_insure(unittest.TestCase):

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

    # 开始投保
    def test_insure(self):
        sleep(6)
        # self.base.to_new_window()
        # 点击我已阅读投保须知并同意
        self.base.click(self.base.find_element(p.buttontwo))
        sleep(6)
        # 滚动页面
        self.base.roll_window_one()
        sleep(3)
        # 填写图形验证码
        self.base.send_keys(self.base.find_element(p.picture_code), picture_code)
        sleep(3)
        # 填写短信验证码
        self.base.send_keys(self.base.find_element(p.message_code), message_code)
        sleep(3)

        # # 选择苏州银行出函机构
        # self.base.click(self.base.find_element(p.click_suzhou))
        # sleep(3)
        # # 选择海城担保担保机构
        # self.base.click(self.base.find_element(p.click_haicheng))
        # sleep(3)
        # # 滑动页面到底部
        # self.base.roll_window_two()
        # sleep(3)
        # # 输入保函差额
        # self.base.send_keys(self.base.find_element(p.money_location), money)
        # sleep(3)
        # # 点击下一步
        # self.base.click(self.base.find_element(p.stepone))
        # sleep(3)
        # # 点击立即投保
        # self.base.click(self.base.find_element(p.insureone))
        # sleep(6)
        # # 点击立即支付
        # self.base.click(self.base.find_element(p.pay_now))
        # sleep(3)
        # self.base.roll_window_two()
        # sleep(3)

        # 选择上海银行出函机构
        self.base.click(self.base.find_element(p.click_shanghai))
        sleep(3)
        # 选择国发担保担保机构
        self.base.click(self.base.find_element(p.click_guofa))
        sleep(3)
        # 滑动页面到底部
        self.base.roll_window_two()
        sleep(3)
        # 输入保函差额
        self.base.send_keys(self.base.find_element(p.money_location), money)
        sleep(3)
        # 点击下一步
        self.base.click(self.base.find_element(p.steptwo))
        sleep(4)
        # 点击立即投保
        self.base.click(self.base.find_element(p.insuretwo))
        sleep(10)
        # 点击确认是否超过开标时间
        # self.base.click(self.base.find_element(p.open_time))
        # sleep(3)
        # self.base.test_Screenshot()
        self.base.click(self.base.find_element(p.click_message_code))
        sleep(60)


if __name__ == '__main__':
    unittest.main()