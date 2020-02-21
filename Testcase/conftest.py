#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/1 14:47
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
# 共享机制的文件名为conftest.py
import pytest
from selenium import webdriver
from layout.qcd_home_layout import Loop
from desired import desired as De
from tedata import qcd_data as AC
@pytest.fixture(scope="class")
def demo():
    print("======================================================================================用例开始=====================================================================================================================")
    yield
    print("======================================================================================用例结束=====================================================================================================================")


@pytest.fixture
def intopop():
    driver = webdriver.Remote(De.url["url"], De.desired_caps)
    yield driver

