# -*- coding:utf-8 -*-
# @Time : 2021/11/25 11:48
# @Author : ASUS
# @File : DoExcel.py

import xlrd

class ReadExcel(object):
    """
    打开excel，读取测试数据
    """
    # 打开Excle，读取某个sheet
    def __init__(self,filename,sheetname):
        self.filename =filename
        datapath = './../data_manage/test_data.xlsx'  # 测试数据的路径
        # print(datapath)
        # 打开测试数据文件data_manage包中的 test_data.xlsx文件
        self.workbook = xlrd.open_workbook(filename)
        self.sheetName = self.workbook.sheet_by_name(sheetname)

    # 获取某个单元格的数据（索引获取）
    def read_excel(self,rownum,colnum):
        value = self.sheetName.cell(rownum,colnum).value
        return value


# #*************************
# # 验证ReadExcel类的正确性
# #*************************
# 获取某个单元格的数据（索引获取）
cellValue = ReadExcel("test_data.xlsx","test_dl").read_excel(1, 0)
print (cellValue)        #运行结果：http://discuz.e70w.com/
