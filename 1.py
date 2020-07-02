f = open("commit.txt", 'r', encoding='utf-8', errors='ignore')  # 打开要处理的文件
data = open("data.txt", 'w+', encoding='utf-8')
lines = f.readlines()
for lines in lines:  # 对TXT 进行逐行读取
    if 'Author' in lines:  # 如果关键字在行中，则输出这行内容
        print(lines, file=data)

'''i = 0
while i < length:
    times = 1
    passwordstr = mylist[i]
    while i+1<=length-1 and mylist[i]==mylist[i+1]:
        times+=1
        i+=1
    print(times,passwordstr)
    i+=1
    '''