# -*- coding:utf-8 -*-
# @Time : 2021/11/24 10:39
# @Author : ASUS
# @File : base_page.py

import logging
from  time import *
from backletter_project_one.utils.DoExcel_Fz import Login_data
from backletter_project_one.config.Page_Element import Page_Element as p
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#将 Test_manage中的 test_data.xlsx 数据导入

#------注册------
zc_mobile_numbe = Login_data.get_zc_mobile_number()
zc_picture_code = Login_data.get_zc_picture_code()
zc_message_code = Login_data.get_zc_message_code()
zc_passwordone  = Login_data.get_zc_passwordone()
zc_passwordtwo  = Login_data.get_zc_passwordtwo()

#------登录------
url = Login_data.get_url()
project = Login_data.get_project()
blocks = Login_data.get_blocks()
picture_code = Login_data.get_picture_code()
message_code = Login_data.get_message_code()
money = Login_data.get_money()

#------申请发票------
# email = Login_data.get_email()  #电子邮箱地址
recipients = Login_data.get_recipients() #收件人
recipients_mobile = Login_data.get_recipients_mobile() #收件人手机号
consignee_address = Login_data.get_consignee_address() #收件地址
registered_address = Login_data.get_registered_address() #注册地址
contact_number = Login_data.get_contact_number() #联系电话
opening_bank = Login_data.get_opening_bank() #开户行
account_number = Login_data.get_account_number() #开户账号


#基础配置
class Base_page():

    #driver对象初始化
    def __init__(self):
        self.driver = webdriver.Chrome()

    #浏览器初始化
    def start_window(self):
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    #隐性等待
    def wait_time(self):
        self.driver.implicitly_wait(10)

    #显性等待
    def webdriverwait(seif):
        seif.wait = WebDriverWait(seif.driver,40)
        # 当元素可见时
        seif.wait.until(EC.visibility_of_element_located(p.buttontwo))

        #执行完成退出
    def quit_window(self):
        self.driver.quit()

    #进入最新的页面
    def to_new_window(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    #页面滚动第一次
    def roll_window_one(self):
        self.roll = 'window.scrollTo(0,800)'
        self.driver.execute_script(self.roll)

    #页面滚动第二次
    def roll_window_two(self):
        self.roll = 'window.scrollTo(0,10000)'
        self.driver.execute_script(self.roll)

    # 点击元素
    def click(self, element):
        element.click()

    # 输入数据
    def send_keys(self, element, text):
        element.send_keys(text)


    #封装元素定位
    def find_element(self, element):
        try:
            type = element[0]
            value = element[1]
            if type == "id" or type == "ID" or type == "Id":
                elem = self.driver.find_element_by_id(value)
            elif type == "name" or type == "NAME" or type == "Name":
                elem = self.driver.find_element_by_name(value)
            elif type == "class" or type == "CLASS" or type == "Class":
                elem = self.driver.find_element_by_class_name(value)
            elif type == "link" or type == "LINK" or type == "link":
                elem = self.driver.find_element_by_link_text(value)
            elif type == "xpath" or type == "Xpath" or type == "Xpath":
                elem = self.driver.find_element_by_xpath(value)
            elif type == "css" or type == "CSS" or type == "Css":
                elem = self.driver.find_element_by_css_selector(value)
            else:
                raise NameError("Please input correct the type parameter!")
        except Exception:
            raise NameError("This element not found!" + str(element))
        return elem


    #截图功能
    def test_Screenshot(self):
        now_time = strftime('%y-%m-%d %H-%M-%S')
        png_folder_path = r'./../report/png/2021-11-22/'
        file_path = png_folder_path + '\\' + now_time + '_Screen.png'
        self.driver.get_screenshot_as_file(file_path)


#日志文件
class Log():
    def __init__(self):
        logging.basicConfig(
            level = logging.INFO,
            # log格式
            format = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt= '%Y-%m-%d %H:%M:%S', #日期格式
            filename= './../report/log/2021-11-22/test.txt',  #日志输出文件
            filemode = 'a'  #追加模式
        )

    def add_log(self, page, func, des):
        out_str = page + func + '----->' + des
        logging.info(out_str)







