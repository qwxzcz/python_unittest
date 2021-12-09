# @Time : 2021/11/22 10:22
# @Author : ASUS
# @File : init_folder.py

import os

def init_folder(data):
    #创建html目录位置
    html_folder_path = './../report/html/'

    #将所创建的子目录添加时间标记
    folder_path =html_folder_path + data

    #判断当前日期目录是否存在，不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    #创建log目录位置
    log_folder_path = './../report/log/'
    folder_path =log_folder_path +data

    # 判断当前日期目录是否存在，不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


    # 创建 png 目录位置
    png_folder_path = './../report/png/'
    folder_path = png_folder_path + data

    # 判断当前日期目录是否存在，不存在则创建
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)


