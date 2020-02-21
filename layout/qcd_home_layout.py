#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 21:18
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from Common.base import Base
from elelocation.qcd_home import Home as HO
class Loop(Base):
    def cs_one(self,mobile,pwd):
        self.click_ele(HO.me,"点击我")
        self.send_text(HO.sjh,mobile,"输入手机号码")
        self.click_ele(HO.xyb,"点击下一步")
        self.send_text(HO.pwd,pwd,"输入密码")
        self.click_ele(HO.qd,"点击确定按钮")
