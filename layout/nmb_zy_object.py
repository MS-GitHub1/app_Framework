#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 12:02
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from elelocation.nmb_zy_page import Zy as ZY
from Common.base import Base
class NMB_ZY(Base):
    # 列表滑动操作
    def lb_tiku(self):
        self.click_ele(ZY.tiku, "点击题库按钮")
        self.get_lb_slide(ZY.tiku, ZY.ISTQB, "huadong")

    def zy_toast(self):
        self.click_ele(ZY.qcb,"点击全程班")
        self.wait_ele(ZY.wv,"等待")
        self.get_blend()
        self.click_ele(ZY.jq,"点击加群按钮")
