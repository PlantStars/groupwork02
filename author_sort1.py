# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:29:21 2020

@author: Rhys
"""

s = []
s1 = open("c.txt", "w+", encoding="utf-8")
f = open("commit.txt", 'r', encoding='utf-8', errors='ignore')  # 打开要处理的文件
data = open("data.txt", 'w+', encoding='utf-8')
lines = f.readlines()
for i in lines:  # 对TXT 进行逐行读取
    if 'Author: ' in i:  # 如果关键字在行中，则输出这行内容
        i1 = i.split(": ")
        i2 = i1[1].split(" <")
        s.append(i2[0])
print(s, file=s1)
