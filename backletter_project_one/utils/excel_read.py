# @Time : 2021/11/22 10:22
# @Author : ASUS
# @File : excel_read.py

#导入读取表格数据插件
from openpyxl import load_workbook

class ParseExcel():
    #声明 ParseExce对象时传入Excel文件路径及表名
    def __init__(self,excel_path,sheetName):
        self.wb = load_workbook(excel_path)
        self.sheet = self.wb[sheetName]

    #将表中数据处理成一维列表
    #此方法用来处理 data_new 表中数据
    def getDataFromSheet(self):
        dataList = []
        for line in self.sheet:
            dataList.append(line[0].value)
        #清除表头数据
        # dataList.pop(0)
            return dataList

    #将表中数据处理成二维列表
    #此方法用来处理 data_sou 表中数据
    #此方法适用于处理传入数据中自带预期结果数据情况
    # def getDataFromSheet_mul(self):
    #     dataList =[]
    #     for line in self.sheet:
    #         tmp_list = []
    #         tmp_list.append(line[0].value)
    #         tmp_list.append(line[1].value)
    #         dataList.append(tmp_list)
    #     #清除表头数据
    #     # dataList.pop(0)
    #     return dataList

if __name__ == '__main__':
    #验证取值正确
    excel_path = './../data_manage/test_data.xlsx'
    sheetName = 'test_dl'
    pe = ParseExcel (excel_path,sheetName)
    print(pe.getDataFromSheet())
    # sheetName = 'data_sou'
    # pr = ParseExcel (excel_path,sheetName)
    # print(pr.getDataFromSheet_mul())




