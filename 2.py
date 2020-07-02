count = open("count.txt", "w+", encoding="utf-8")
with open('data0.txt', 'r', encoding='utf-8') as f:
    line = f.read().strip()
    author_name = line.split("\n")  # 以换行符分隔
    print(author_name, file=count)
