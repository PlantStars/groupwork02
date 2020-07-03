with open(r"count.txt", mode="r", encoding="utf-8")as f:
    data = f.read()
data1 = eval(data)

a = []
for i in data1:
    i = str(i)
    if "', " in i:
        i1 = i.split("', ")
    else:
        i1=i.split("\", ")
    i2 = i1[1].replace(")", "")
    i3 = int(i2)
    a.append(i3)

import random

random.shuffle(a)
length = len(a)


n = 0
b = []
for i in range(length):
    n += 1
    b.append(n)

# import matplotlib.pyplot as plt
#
# plt.scatter(b, a)
# plt.show()


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

with open(r"commit.txt", mode="r", encoding="utf-8")as f:  # input your data file
    data = f.read()
m = []
m = data.split("Author: ")
m.remove(m[0])

hang = []  # 切割行
author = {}  # 作者
n = 0
for i1 in m:
    n += 1
    v0 = 0
    v2 = 0
    hang = i1.split("\n")

    if hang[0] not in author:
        v0 = 1
        if "fix" in i1:
            v2 = 1
        author[hang[0]] = [v0, v2]
    else:
        author[hang[0]][0] += 1
        if "fix" in i1:
            author[hang[0]][1] += 1
    hang = []
    v0 = 0
    v2 = 0

am = []
fix = []
bf = list(author.values())
for i in bf:
    am.append(i[0])
    fix.append(i[1])
am2 = []
for i in a:
    temp = []
    temp.append(i)
    am2.append(temp)
fix2 = []
for i in fix:
    temp2 = []
    temp2.append(i)
    fix2.append(temp2)
while len(am2) < len(fix2):
    fix.pop()
    fix2.pop()

lm = LinearRegression()
lm.fit(am2, fix2)
print("The deterministic coefficient R^2 of the equation：", lm.score(am2, fix2))
print("Linear regression algorithm w value：", lm.coef_)
print("Linear regression algorithm b value：", lm.intercept_)
fig = plt.figure()  # key and value as axis
plt.scatter(a, fix, color='r', marker='+')
plt.plot(am2, lm.predict(am2), color='green', linewidth=3)
plt.show()
