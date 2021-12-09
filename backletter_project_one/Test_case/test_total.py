# -*- coding:utf-8 -*-
# @Time : 2021/12/3 15:32
# @Author : ASUS
# @File : test_total.py

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

#---------------注册账号---------------

    def test_1_register(self):
        sleep(3)
        # 点击用户注册
        self.base.click(self.base.find_element(p.zc_register))
        sleep(3)
        # 输入手机号
        self.base.send_keys(self.base.find_element(p.zc_mobile_number), zc_mobile_numbe)
        sleep(3)
        # 输入图形验证码
        self.base.send_keys(self.base.find_element(p.zc_picture_code), zc_picture_code)
        sleep(3)
        # 点击获取短信验证码
        self.base.click(self.base.find_element(p.zc_verify))
        sleep(3)
        try:
            self.assertEqual(self.base.find_element(p.zc_prompt_message).text, '手机号已注册，请直接登录')
            self.base.click(self.base.find_element(p.zc_denglu))
            # self.tearDown()

        except AssertionError as e:
            self.zc = str(e)
            self.log.add_log('执行结果:', self.zc, '执行失败')

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


#订购标段---开始投保---开具发票

#---------------订购标段---------------

    def test_2_place_order(self):
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

#---------------开始投保---------------

        # 点击我已阅读投保须知并同意
        self.base.to_new_window()
        sleep(3)
        self.base.click(self.base.find_element(p.buttontwo))
        sleep(3)
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
        #
        # sleep(3)
        # # 滑动页面到底部
        # self.base.roll_window_two()
        # sleep(3)
        # # 输入保函差额
        # self.base.send_keys(self.base.find_element(p.money_location), money)
        # sleep(3)
        # # 点击下一步
        # self.assertEqual(self.base.find_element(p.stepone).text, '下一步')
        # self.base.click(self.base.find_element(p.stepone))
        # sleep(4)
        # # 点击立即投保
        # self.base.click(self.base.find_element(p.insureone))

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
        sleep(3)
        # 点击立即投保
        self.base.click(self.base.find_element(p.insuretwo))
        sleep(10)
        # 点击确认是否超过开标时间
        # self.base.click(self.base.find_element(p.open_time))
        # sleep(3)
        # self.base.test_Screenshot()
        self.base.click(self.base.find_element(p.click_message_code))
        sleep(60)

#---------------开具发票---------------

        #下载保函
        self.base.click(self.base.find_element(p.download_backletter))
        sleep(3)
        self.base.roll_window_two()
        sleep(3)
        # 点击申请发票
        self.base.click(self.base.find_element(p.apply_invoice))
        sleep(3)

        # #申请电子发票
        # self.base.click(self.base.find_element(p.electronic_invoice))
        # sleep(3)
        # # 输入电子发票地址(非纸质)
        # # self.base.send_keys(self.base.find_element(p.email), email)
        # # sleep(3)
        # # 点击提交
        # self.base.click(self.base.find_element(p.submit_one))
        # sleep(6)
        # self.base.test_Screenshot()
        # 下载电子发票
        # self.base.click(self.base.find_element())

        #申请普通发票(纸质)
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



    # 开始投保
    # def test_3_insure(self):
    #
    #     #点击我已阅读投保须知并同意
    #     self.base.to_new_window()
    #     sleep(3)
    #     self.base.click(self.base.find_element(p.buttontwo))
    #     sleep(3)
    #     #滚动页面
    #     self.base.roll_window_one()
    #     sleep(3)
    #     #填写图形验证码
    #     self.base.send_keys(self.base.find_element(p.picture_code), picture_code)
    #     sleep(3)
    #     #填写短信验证码
    #     self.base.send_keys(self.base.find_element(p.message_code), message_code)
    #     sleep(3)
    #
    #     # # 选择苏州银行出函机构
    #     # self.base.click(self.base.find_element(p.click_suzhou))
    #     # sleep(3)
    #     # # 选择海城担保担保机构
    #     # self.base.click(self.base.find_element(p.click_haicheng))
    #     #
    #     # sleep(3)
    #     # # 滑动页面到底部
    #     # self.base.roll_window_two()
    #     # sleep(3)
    #     # # 输入保函差额
    #     # self.base.send_keys(self.base.find_element(p.money_location), money)
    #     # sleep(3)
    #     # # 点击下一步
    #     # self.assertEqual(self.base.find_element(p.stepone).text, '下一步')
    #     # self.base.click(self.base.find_element(p.stepone))
    #     # sleep(4)
    #     # # 点击立即投保
    #     # self.base.click(self.base.find_element(p.insureone))
    #
    #
    #     #选择上海银行出函机构
    #     self.base.click(self.base.find_element(p.click_shanghai))
    #     sleep(3)
    #     # 选择国发担保担保机构
    #     self.base.click(self.base.find_element(p.click_guofa))
    #     sleep(3)
    #     # 滑动页面到底部
    #     self.base.roll_window_two()
    #     sleep(3)
    #     # 输入保函差额
    #     self.base.send_keys(self.base.find_element(p.money_location), money)
    #     sleep(3)
    #     # 点击下一步
    #     self.base.click(self.base.find_element(p.steptwo))
    #     sleep(3)
    #     # 点击立即投保
    #     self.base.click(self.base.find_element(p.insuretwo))
    #     sleep(10)
    #     # 点击确认是否超过开标时间
    #     # self.base.click(self.base.find_element(p.open_time))
    #     # sleep(3)
    #     # self.base.test_Screenshot()
    #     self.base.click(self.base.find_element(p.click_message_code))
    #     sleep(60)
    #
    #
    # 开具发票
    # def test_4_apply_invoice(self):
    #
    #     # 下载保函
    #     self.base.click(self.base.find_element(p.download_backletter))
    #     sleep(3)
    #     self.base.roll_window_two()
    #     sleep(3)
    #     # 点击申请发票
    #     self.base.click(self.base.find_element(p.apply_invoice))
    #     sleep(3)
    #
    #     # #申请电子发票
    #     # self.base.click(self.base.find_element(p.electronic_invoice))
    #     # sleep(3)
    #     # # 输入电子发票地址(非纸质)
    #     # # self.base.send_keys(self.base.find_element(p.email), email)
    #     # # sleep(3)
    #     # # 点击提交
    #     # self.base.click(self.base.find_element(p.submit_one))
    #     # sleep(6)
    #     # self.base.test_Screenshot()
    #     # 下载电子发票
    #     # self.base.click(self.base.find_element())
    #
    #     #申请普通发票(纸质)
    #     self.base.click(self.base.find_element(p.regular_invoice))
    #     sleep(3)
    #     # 输入收件人
    #     self.base.send_keys(self.base.find_element(p.recipients), recipients)
    #     sleep(3)
    #     # 输入收件人手机号
    #     self.base.send_keys(self.base.find_element(p.recipients_mobile), recipients_mobile)
    #     sleep(3)
    #     # 输入收件地址
    #     self.base.send_keys(self.base.find_element(p.consignee_address), consignee_address)
    #     sleep(3)
    #     # 输入注册地址
    #     self.base.send_keys(self.base.find_element(p.registered_address), registered_address)
    #     sleep(3)
    #     # 输入联系电话
    #     self.base.send_keys(self.base.find_element(p.contact_number), contact_number)
    #     sleep(3)
    #     # 输入开户行
    #     self.base.send_keys(self.base.find_element(p.opening_bank), opening_bank)
    #     sleep(3)
    #     # 输入开户账号
    #     self.base.send_keys(self.base.find_element(p.account_number), account_number)
    #     sleep(3)
    #     # 点击提交
    #     self.base.click(self.base.find_element(p.submit_two))
    #     sleep(6)
    #     # 查看收件人信息
    #     self.base.click(self.base.find_element(p.check_recipients_information))
    #     sleep(3)
    #     self.base.test_Screenshot()



if __name__ == '__main__':
    # 构造测试集
    # suite = unittest.TestSuite()
    # suite.addTest(Test_register("test_1_register"))
    # # 执行测试
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()

