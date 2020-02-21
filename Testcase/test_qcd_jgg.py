#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 16:36
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from desired import desired as De
from appium import webdriver
import pytest
from tedata import qcd_data as AC
from layout.qcd_wo_page import Nine
from layout.qcd_home_layout import Loop
@pytest.fixture
def init_dri():
    driver = webdriver.Remote(De.url["url"], De.desired_caps)
    Loop(driver).cs_one(AC.name["name"], AC.name["pwd"])
    lc = Nine(driver)
    yield {"driver":driver,"lc":lc}
    
class Test_jgg():
    @pytest.mark.usefixtures("demo")
    @pytest.mark.usefixtures("init_dri")
    def test_jgg_one(self,init_dri):
        init_dri["lc"].nine_ge()
