# @Time : 2021/11/22 10:18
# @Author : ASUS
# @File : test_baidu_new.py

import unittest
import ddt
from time import sleep
from backletter_project_one.utils.excel_read import ParseExcel
from backletter_project_one.utils.base_page import *
#导入data_manage模块 test_data.xlsx的测试数据
excelPath = './../data_manage/test_data.xlsx'
sheetName = 'test_dl'
excel =ParseExcel(excelPath,sheetName)

#使用ddt方式循环导入数据
@ddt.ddt
class Test_baidu_News(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.base = Base_page()
        self.base.start_window()
        # self.log = Log()

    @classmethod
    def tearDownClass(self):
        self.base.quit_window()

    def setUp(self):
        self.base.enter_window()
        sleep(2)

    def tearDown(self):
        pass

    @ddt.data(* excel.getDataFromSheet())
    def test_dl(self,data):
        '''搜索方式'''
        # self.driver.find_element_by_id('ww').send_keys(data)
        # sleep(2)
        # self.driver.find_element_by_id('s_btn_wr').click()
        # sleep(2)
        # self.assertEqual('百度资讯搜索_'+ data ,self.driver.title)
        # self.log.add_log(data,'用例执行成功')
        self.driver.find_element_by_xpath('//*[@id="otherTable"]/tbody/tr[2]/td[5]/button').click()
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div/button[2]').click()
        sleep(2)
        self.base.to_last_window()
        self.driver.find_element_by_xpath('//*[@id="ice-container"]/div/div/div/div/div/div/div[5]/div/div[1]/div[2]/span/input').send_keys(data)
        sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="ice-container"]/div/div/div/div/div/div/div[5]/div/div[2]/div[2]/span/input').send_key(data)
        # sleep(2)
        # self.driver.find_element_by_xpath('//*[@id="ice-container"]/div/div/div/div/div/div/div[5]/div/div[3]/div[2]/span/input').send_key(data)
        # sleep(2)
        self.driver.find_element_by_class_name('TenderNotice--img_list--1H-j4eM/li[1]').click()


if __name__ == '__main__':
    unittest.main()