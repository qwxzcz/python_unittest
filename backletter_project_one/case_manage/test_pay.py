# @Time : 2021/11/22 10:19
# @Author : ASUS
# @File : test_baidu_sou.py

import unittest
import ddt
from time import sleep
from backletter_project_one.utils.excel_read import ParseExcel
from backletter_project_one.utils.base_page import Log

#导入data_manage模块 test_data.xlsx的测试数据
excelPath = './../data_manage/test_data.xlsx'
sheetName = 'data_sou'
excel =ParseExcel(excelPath,sheetName)


#使用ddt方式循环导入数据
@ddt.ddt
class Test_baidu_Search(unittest.TestCase):
    '''百度搜索用例'''

    @classmethod
    def setUpClass(self):
        self.Base_page.start_window()
        self.log = Log()

    @classmethod
    def tearDownClass(self):
        self.Base_page.quit_window()

    def setUp(self):
        self.Base_page.enter_window()
        sleep(2)

    def tearDown(self):
        pass

    # @ddt.data(*excel.getDataFromSheet_mul())
    # def test_sou(self,data):
    #     '''搜索方式'''
    #     try:
    #         self.driver.find_element_by_id('kw').send_keys(data[0])
    #         sleep(2)
    #         self.driver.find_element_by_id('su').click()
    #         sleep(2)
    #         self.assertEqual(data[0] + '_百度搜索', self.driver.title)
    #     except AssertionError as e:
    #         self.log.add_log(data[0],data[1],format(e))
    #         self.assertEqual(data[0] + '_百度搜索', self.driver.title)
    #     else:
    #         self.log.add_log(data[0],data[1], '用例执行成功')

if __name__ == '__main__':
    unittest.main()