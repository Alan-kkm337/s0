# wordcount.py
# 目标：统计 sample.txt 中的词频，打印出现最多的 10 个单词

# 第 1 步：读取文件
# 提示：with open('sample.txt', encoding='utf-8') as f:
#          text = f.read()
with open('sample.txt',encoding='utf-8') as f:
    text = f.read()
# 第 2 步：转小写 + 按空白切分成单词列表
# 提示：.lower() 和 .split()
words = text.split()
# 第 3 步：用字典计数
# 提示：counts = {}
#      每遇到一个词：counts[word] = counts.get(word, 0) + 1
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
# 第 4 步：排序取前 10
# 提示：sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
top_words = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:10]
# 第 5 步：打印，格式 单词 + 空格 + 次数
for word, count in top_words:
   print(f"{word} {count}")