import csv
import matplotlib.pyplot as plt
import re

data = []
date = []
time_zone = []
time = []


def date_sort(date, patt):
    for i in range(len(date) - 1):
        for x in range(i + 1, len(date)):
            j = 1
            while j < 4:
                lower = re.search(patt, date[i]).group(j)
                upper = re.search(patt, date[x]).group(j)
                if int(lower) < int(upper):
                    j = 4
                elif int(lower) == int(upper):
                    j += 1
                else:
                    date[i], date[x] = date[x], date[i]
                    j = 4
    return date


def out_put_sort(zone, out_put_key=[], out_put_value=[]):
    for i in dic_all[zone]:
        out_put_key.append(list(i.keys())[0])
    out_put_key = date_sort(out_put_key, patt='(\d+)-(\d+)')
    for i in out_put_key:
        for k in dic_all[zone]:
            if list(k.keys())[0] == i:
                out_put_value.append(k[list(k.keys())[0]])
                break
    return out_put_key, out_put_value


with open("clean_data.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        date.append(row[0])
        time_zone.append(row[1])
        time.append(row[2])
        data.append([row[0], row[1], row[2]])

# 统计
# 统计每月人数
dic_datetime = {}
for i in data:
    if i[0] not in dic_datetime:
        dic_datetime[i[0]] = int(i[2])
    else:
        dic_datetime[i[0]] += int(i[2])

datetime_key = list(dic_datetime.keys())
datetime_key = date_sort(datetime_key, patt='(\d+)-(\d+)')
datetime_value = []
for i in datetime_key:
    datetime_value.append(dic_datetime[i])
# 统计地区总人数
dic_timezonetime = {}
for i in data:
    if i[1] not in dic_timezonetime:
        dic_timezonetime[i[1]] = int(i[2])
    else:
        dic_timezonetime[i[1]] += int(i[2])
timezonetime_key = list(dic_timezonetime.keys())
timezonetime_key = list(map(int, timezonetime_key))
timezonetime_key.sort()
timezonetime_key = list(map(str, timezonetime_key))
timezonetime_value = []
for i in timezonetime_key:
    timezonetime_value.append(dic_timezonetime[i])
# 统计每月地区人数
dic_all = {}
lst_all = []
for i in data:
    lst_all.append({i[1]: {i[0]: i[2]}})
for i in lst_all:
    if list(i.keys())[0] not in dic_all:
        dic_all[list(i.keys())[0]] = [i[list(i.keys())[0]]]
    else:
        dic_all[list(i.keys())[0]].append(i[list(i.keys())[0]])

res_tuple = out_put_sort("-600")

"""
#绘图
plt.plot(res_tuple[0],res_tuple[1])
plt.show()
"""

# 数据输出
with open('data.csv', 'w', newline="") as csvFile:
    writer = csv.writer(csvFile, delimiter='\t')
    for i in res_tuple[1]:
        writer.writerow((str(i),))
