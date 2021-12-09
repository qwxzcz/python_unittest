# -*- coding:utf-8 -*-
# @Time : 2021/11/25 11:48
# @Author : ASUS
# @File : DoExcel.py

import xlrd
import os
from backletter_project_one.config import globalconfig
data_paths = globalconfig.data_path   #测试数据的相对路径

class ReadExcel(object):
    """
    打开excel，读取测试数据
    """
    # 打开Excle，读取某个sheets
    def __init__(self,filename,sheetname):
        datapath = os.path.join(data_paths,filename) #C:\python-3.7.3-amd64\backletter_project_one\Test_manage\test_data.xlsx

        # 打开测试数据文件 data_manage包中的 test_data.xlsx文件

        self.workbook = xlrd.open_workbook(datapath)
        self.sheetName = self.workbook.sheet_by_name(sheetname)


    # 获取某个单元格的数据（索引获取）
    def read_excel(self,rows,cols):
        value = self.sheetName.cell(rows,cols).value
        return value


# 获取某个单元格的数据（索引获取）
# path = ReadExcel("test_data.xlsx","test_dl").read_excel(0,0)
# print(path)


# datapath = os.path.join(data_paths,'test_data.xlsx')
# print(datapath)