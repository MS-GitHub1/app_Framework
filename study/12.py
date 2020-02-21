#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:15
# @Author  : Lynn
# @Site    : 
# @Software: PyCharm
b = ['case_id', 'data', 'expected']
a = [[1, '(1, 2)', 3], [2, "(1, 'a')", 'None'], [3, "('a', 'b')", 'None'], [4, '(5, 0)', 5]]
for c in a:
    print(dict(zip(b,c)))

