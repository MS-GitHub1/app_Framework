#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/14 11:02
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
import pytest
import time
def add(a,b):
    try:
        return a + b
    except Exception as e:
        return e
a = {"l":1,"p":2,"o":3},{"l":2,"p":3,"o":6},{"l":3,"p":4,"o":7},{"l":4,"p":5,"o":9}
@pytest.mark.parametrize("test_info",a)
def test_add(test_info):
    time.sleep(1)
    c = add(test_info["l"],test_info["p"])
    assert c ==test_info["o"]
