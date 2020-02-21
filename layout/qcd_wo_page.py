#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 16:41
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from Common.base import Base
from elelocation.qcd_me_page import Me_page as MO
class Nine(Base):
    def nine_ge(self):
        self.click_ele(MO.anquan,"点击安全中心")
        self.click_ele(MO.ssmm,"点击手势密码")
        self.click_ele(MO.sz,"点击设置手势密码")
        self.click_ele(MO.cjsj, "点击创建手势密码")
        self.click_ele(MO.ssqd, "点击确定按钮")
        self.wait_ele(MO.jx,"等待继续按钮")
        self.nine_squared(MO.tuan,"画九宫格")