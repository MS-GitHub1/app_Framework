#!/usr/bin/python3
# -*- coding: utf-8 -*-
#Author: xiaojian
#Time: 2018/11/28 17:04
from os.path import *
import os
# 获取上级目录绝对路径
# 配置文件的路径
def picture_path():
    dir_path = dirname(dirname(abspath(__file__)))
    csyl_path = os.path.join(dir_path,"picture")
    return csyl_path

def log_path():
    dir_path = dirname(dirname(abspath(__file__)))
    log_path = os.path.join(dir_path, "log")
    return log_path

def report_path():
    dir_path = dirname(dirname(abspath(__file__)))
    cscase_path = os.path.join(dir_path, "reportone")
    return cscase_path
picture_path = picture_path()
log = log_path()
report_path = report_path()
print(report_path)
