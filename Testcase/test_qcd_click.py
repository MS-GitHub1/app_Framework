#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 17:30
# @Author  : Lynn
# @Site    :
# @Software: PyCharm
from desired import desired as De
from appium import webdriver
import pytest
from layout.qcd_home_layout import Loop
from tedata import qcd_data as AC
@pytest.fixture
def init_driver():
    driver = webdriver.Remote(De.url["url"], De.desired_caps)
    lp = Loop(driver)
    yield {"lp":lp}

@pytest.mark.usefixtures("demo")
class Testlogin():
    def test_login_1(self,init_driver):
        init_driver["lp"].cs_one(AC.name["name"],AC.name["pwd"])
