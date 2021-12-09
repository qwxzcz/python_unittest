# -*- coding:utf-8 -*-
# @Time : 2021/12/7 15:50
# @Author : ASUS
# @File : Page_Element_two.py

class Page_Element:

    #定义注册页面的元素
    # 点击用户注册
    zc_register = ("xpath", "//*[@class='regFor']/span[2]")
    # 输入手机号码
    zc_mobile_number =("id", "loginForm_phoneNum")
    #输入图形验证码
    zc_picture_code =("id", "loginForm_code")
    # 点击获取短信验证码
    zc_verify =("xpath", "//*[@class='ant-form-item-control']/span/a")
    # 提示:手机号已经注册
    zc_prompt_message = ("class", "ant-message-notice-content")
    # 点击登录 (已经注册过)
    zc_denglu = ("xpath", "//*[@class='titleDocument']/a")
    #输入短信验证码
    zc_message_code =("id", "loginForm_phCode")
    # 输入登录密码
    zc_passwordone=("id", "loginForm_password")
    # 确认登陆密码
    zc_passwordtwo=("id", "loginForm_conPassword")
    # 显示提示信息,验证码不正确
    zc_verify_code = ("class", "ant-message-notice-content")
    # 点击立即注册
    zc_button=("xpath", "//button[@class='ant-btn ant-btn-primary']")


    #定义下单页面的元素
    # 输入手机号码
    mobile_number = ("xpath", "//*[@class='psw']/input")
    # 输入登录密码
    password = ("xpath", "//*[@class='psw']/span/input")
    # 点击立即登录
    log_in = ("xpath", "//button[@class='ant-btn ant-btn-primary']")

    # 搜索项目名称
    Search_project= ("class", "ant-input")
    # 点击查询项目
    Click_inquire_one = ("xpath", "//*[@class='search']/button[1]")
    # 点击查看项目
    Check_project = ("xpath", "//tbody[@class='ant-table-tbody']/tr/td[4]/span/a")

    # 搜索标段名称
    Search_blocks= ("class", "ant-input")
    # 点击查询标段
    Click_inquire_two = ("xpath", "//*[@class='search']/button[1]")
    # 点击申请标段
    Application_blocks = ("xpath", "//*[@class='bottom']/div[7]/button")
    # 点击确定进入下一步
    Next_step = ("xpath", "//*[@class='btn']/button[2]")


    #定义投保页面的元素
    # 点击不同意，取消退保
    # buttonone = ("xpath", "//*[@class='next-dialog-footer next-align-center']/div/button[1]")

    # 点击同意，我知道了
    buttontwo = ("xpath", "//*[@class='next-dialog-footer next-align-center']/div/button[2]")
    # 输入图形验证码
    picture_code = ("xpath", "//*[@class='TenderNotice--info_sub--1SkkUPh']/div[2]/div[2]/span/input")
    # 输入短信验证码
    message_code = ("xpath", "//*[@class='TenderNotice--info_sub--1SkkUPh']/div[3]/div[2]/span/input")

    # 选择苏州银行出函机构
    click_suzhou = ("xpath", "//*[@class='TenderNotice--info_sub--1SkkUPh']/div/div/div/ul/li[1]")
    # 选择海城担保担保机构
    click_haicheng = ("xpath", "//*[@class='TenderNotice--info_sub--1SkkUPh']/div/ul/li")
    # 点击下一步按钮
    stepone = ("xpath", "//*[@class='TenderNotice--btn_box--3qK_hLS']/button[2]")
    # 点击立即投保按钮
    insureone = ("xpath", "//*[@class='TenderNotice--btn_box--3qK_hLS']/button[2]")
    # 点击立即支付
    pay_now = ("xpath", "//*[@class='TenderConfirm--button1--1pBMH5M']/button")





    # 选择上海银行出函机构
    click_shanghai = ("xpath", "//*[@class='TenderNotice--info_sub--1SkkUPh']/div/div/div/ul/li[2]")
    # 选择国发担保担保机构
    click_guofa = ("xpath", "//*[@class='TenderNotice--info_sub--1SkkUPh']/div/ul/li")
    # 输入保函差额金额
    money_location = ("id", "marginDom")
    # 点击下一步按钮
    steptwo = ("xpath", "//*[@class='TenderNotice--btn_box--3qK_hLS']/button[2]")
    # 点击立即投保按钮
    insuretwo = ("xpath", "//*[@class='TenderNotice--btn_box--3qK_hLS']/button[2]")
    # 预计开标时间提醒
    # open_time = ("xpath", "//button[@class='next-btn next-medium next-btn-primary']")
    # 点击查看订单详情
    click_message_code = ("class", "next-btn-helper")


    #定义支付页面元素

    #定义投保成功页面元素
    # 点击下载保函
    download_backletter=("xpath", "//*[@class='TenderConfirm--button1--1pBMH5M']/button")
    # 申请发票
    apply_invoice=("xpath", "//*[@id='invoiceInfo']/div/button")
    # 选择电子发票(非纸质)
    electronic_invoice=("xpath", "//*[@class='next-radio-group next-radio-group-hoz']/label[1]/span[1]/input")
    # 输入电子邮箱地址
    email = ("id", "email")
    # 点击提交
    submit_one = ("xpath", "//*[@class='next-col next-col-14 next-form-item-control']/button")
    # 下载电子发票
    # download_electronic_invoice = ("xpath", "//*[@id='invoiceInfo']/span[2]/button")


    # 选择普通发票(纸质)
    regular_invoice = ("xpath", "//*[@class='next-radio-group next-radio-group-hoz']/label[2]/span[1]/input")
    # 点击收件人
    recipients = ("id", "addressee")
    # 点击收件人手机号
    recipients_mobile = ("id", "addresseePhoneNo")
    # 点击收件地址
    consignee_address = ("id", "receiveAddress")
    # 点击注册地址
    registered_address = ("id", "addressInfo")
    # 点击联系电话
    contact_number = ("id", "phoneNo")
    # 点击开户行
    opening_bank = ("id", "openBank")
    # 点击开户账号
    account_number = ("id", "bankAccountNo")
    # 点击提交
    submit_two = ("xpath", "//*[@class='next-col next-col-14 next-form-item-control']/button")
    # 查看收件人信息
    check_recipients_information = ("xpath", "//*[@id='invoiceInfo']/div/button")