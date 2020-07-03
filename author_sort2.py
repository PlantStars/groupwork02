# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:29:21 2020

@author: Rhys
"""

count0 = open('count.txt', 'w', encoding='utf-8')
with open('c.txt', mode="r", encoding='utf-8') as fh:
    lo = fh.read()
li = eval(lo)

count = {}
for i in li:
    if i not in count:
        count[i] = 1
    else:
        count[i] += 1

print(sorted(count.items(), key=lambda d: d[1], reverse=True), file=count0)
