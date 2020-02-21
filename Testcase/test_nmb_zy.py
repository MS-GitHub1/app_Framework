#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 12:04
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
import pytest
from layout.nmb_zy_object import NMB_ZY
from desired import desired as De
from appium import webdriver
@pytest.fixture
def zy_driver():
    driver = webdriver.Remote(De.url["url"], De.desired_nmb)
    zy = NMB_ZY(driver)
    yield {"zy":zy}

class Test_zy():
    @pytest.mark.usefixtures("demo")
    @pytest.mark.usefixtures("zy_driver")

    def test_taose(self,zy_driver):
        zy_driver["zy"].zy_toast()

