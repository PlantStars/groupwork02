s1 = open('count.txt', encoding='utf-8')
count1 = open('count1.txt', 'w', encoding='utf-8')
count2 = open('count2.txt', 'w', encoding='utf-8')

with open('count.txt', encoding='utf-8') as fh:
    li = fh.readlines()
    fh.close()

count = {}
for i in li:
    li2 = i.split(',')
    for j in li2:
        if j not in count:
            count[j] = 1
        else:
            count[j] += 1
print(count, file=count1)
print(sorted(count.items(), key=lambda d: d[1], reverse=True), file=count2)
# key_sorted_result = sorted(count.items(), key=lambda item: item[0], reverse=True)  # 按key进行降序
# print(key_sorted_result, file=count2)
# # 利用函数进行排序
# items = list(count.items())
# items.sort(key=lambda x: x[1], reverse=True)
# for i in range(1):
#     word, c = items[0]
#     print(word)
#
# # 自行排序
# max_name, max_sum = "", 0
# for j in count:
#     if count[j] > max_sum:
#         max_sum, max_name = count[j], j
# print(max_name)


# def complete_author(self):
#     auth, time, note = self.get_auti()
#     for i in range(0, len(auth)):
#         if auth[i] in self.author.keys():
#             self.author[auth[i]].append(time[i])
#         else:
#             self.author[auth[i]] = [time[i]]
#     for i in range(0, len(auth)):
#         if auth[i] in self.author.keys():
#             self.author[auth[i]].append(note[i])
#         else:
#             self.author[auth[i]] = [note[i]]
#     return self.author
#
#
# complete_author(s1)
