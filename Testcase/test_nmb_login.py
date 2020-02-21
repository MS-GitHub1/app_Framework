#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 17:53
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
from desired import desired as De
from appium import webdriver
import pytest
from layout.nmb_login_page import NMB_login as Lp
from tedata import qcd_data as AC
@pytest.fixture
def ini_drive():
    driver = webdriver.Remote(De.url["url"], De.desired_nmb)
    lp = Lp(driver)
    yield {"lp":lp}

class Test_nmb_home():
    @pytest.mark.usefixtures("demo")
    @pytest.mark.usefixtures("ini_drive")

    # 登录成功
    def test_login_1(self,ini_drive):
        ini_drive["lp"].hq_xx()
        if ini_drive["lp"].success_lo() == "Mr Feng":
            ini_drive["lp"].cl_bu()
            ini_drive["lp"].nmb_login(AC.mobile["mobile"],AC.mobile["pwd"])
            assert ini_drive["lp"].success_lp() == AC.mobile["check"]
        else:
            ini_drive["lp"].nmb_login(AC.mobile["mobile"], AC.mobile["pwd"])
            assert ini_drive["lp"].success_lp() == AC.mobile["check"]

    # 登录失败用户名密码错误 为空
    @pytest.mark.parametrize("test_info",AC.mobile_failed)
    def test_login_2(self,ini_drive,test_info):
        ini_drive["lp"].hq_xx()
        if ini_drive["lp"].success_lo() == "Mr Feng":
            ini_drive["lp"].cl_bu()
            ini_drive["lp"].nmb_login(test_info["mobile"],test_info["pwd"])
            assert ini_drive["lp"].success_ts == test_info["check"]
        else:
            ini_drive["lp"].nmb_login(test_info["mobile"], test_info["pwd"])
            assert ini_drive["lp"].success_ts == test_info["check"]















