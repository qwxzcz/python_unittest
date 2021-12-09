# -*- coding:utf-8 -*-
# @Time : 2021/11/25 11:55
# @Author : ASUS
# @File : DoExcel_Fz.py

from backletter_project_one.utils import DoExcel

#此模块用于把Excel表格中的数据进行封装
class Login_data(object):

    #获取测试环境地址
    @staticmethod
    def get_url():
        get_url = DoExcel.ReadExcel("test_data.xlsx", "test_dl").read_excel(1, 0)
        return get_url

    #---------------注册----------------
    #获取手机号码
    @staticmethod
    def get_zc_mobile_number():
        get_zc_mobile_number = DoExcel.ReadExcel("test_data.xlsx", "test_zc").read_excel(1, 0)
        return get_zc_mobile_number

    #获取图形验证码
    @staticmethod
    def get_zc_picture_code():
        get_zc_picture_code = DoExcel.ReadExcel("test_data.xlsx", "test_zc").read_excel(1, 1)
        return get_zc_picture_code

    #获取短信验证码
    @staticmethod
    def get_zc_message_code():
        get_zc_message_code = DoExcel.ReadExcel("test_data.xlsx", "test_zc").read_excel(1, 2)
        return get_zc_message_code

    #获取登陆密码
    @staticmethod
    def get_zc_passwordone():
        get_zc_passwordone = DoExcel.ReadExcel("test_data.xlsx", "test_zc").read_excel(1, 3)
        return get_zc_passwordone

    #获取确认登陆密码
    @staticmethod
    def get_zc_passwordtwo():
        get_zc_passwordtwo = DoExcel.ReadExcel("test_data.xlsx", "test_zc").read_excel(1, 4)
        return get_zc_passwordtwo

    #--------------登录投保--------------
    #获取项目名称
    @staticmethod
    def get_project():
        get_project = DoExcel.ReadExcel("test_data.xlsx", "test_dl").read_excel(2, 1)
        return get_project

    #获取标段名称
    @staticmethod
    def get_blocks():
        get_blocks = DoExcel.ReadExcel("test_data.xlsx", "test_dl").read_excel(2, 2)
        return get_blocks

    #获取图形验证码
    @staticmethod
    def get_picture_code():
        get_picture_code = DoExcel.ReadExcel("test_data.xlsx", "test_dl").read_excel(2, 3)
        return get_picture_code

    #获取短信验证码
    @staticmethod
    def get_message_code():
        get_message_code = DoExcel.ReadExcel("test_data.xlsx","test_dl").read_excel(2, 4)
        return get_message_code

    #获取金额
    @staticmethod
    def get_money():
        get_money = DoExcel.ReadExcel("test_data.xlsx","test_dl").read_excel(2, 5)
        return get_money

    #--------------投保成功--------------
    #------申请电子发票(非纸质)------
    #获取电子邮箱地址
    @staticmethod
    def get_email():
        get_email = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 0)
        return get_email


    #------申请普通发票(纸质)-----
    # 获取收件人
    @staticmethod
    def get_recipients():
        get_recipients = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 1)
        return get_recipients

    # 获取收件人手机号
    @staticmethod
    def get_recipients_mobile():
        get_recipients_mobile = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 2)
        return get_recipients_mobile

    # 获取收件地址
    @staticmethod
    def get_consignee_address():
        get_consignee_address = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 3)
        return get_consignee_address

    # 获取注册地址
    @staticmethod
    def get_registered_address():
        get_registered_address = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 4)
        return get_registered_address

    # 获取联系电话
    @staticmethod
    def get_contact_number():
        get_contact_number = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 5)
        return get_contact_number

    # 获取开户行
    @staticmethod
    def get_opening_bank():
        get_opening_bank = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 6)
        return get_opening_bank

    # 获取开户账号
    @staticmethod
    def get_account_number():
        get_account_number = DoExcel.ReadExcel("test_data.xlsx", "test_invoice").read_excel(1, 7)
        return get_account_number




if __name__ == '__main__':
    l = Login_data()
    # ---------------注册----------------
    # print(l.get_zc_mobile_number())
    # print(l.get_zc_picture_code())
    # print(l.get_zc_message_code())
    # print(l.get_zc_passwordone())
    # print(l.get_zc_passwordtwo())

    # --------------登录投保--------------
    # print(l.get_url())
    # print(l.get_project())
    # print(l.get_blocks())
    # print (l.get_picture_code())
    # print (l.get_message_code())
    # print (l.get_money())

    # --------------投保成功--------------
    # print(l.get_email())
    # print(l.get_recipients())
    # print(l.get_recipients_mobile())
    # print(l.get_consignee_address())
    # print (l.get_registered_address())
    # print (l.get_contact_number())
    # print (l.get_opening_bank())
    # print (l.get_account_number())