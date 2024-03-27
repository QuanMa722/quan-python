
"""

baidu_stopwords  百度停用词表
cn_stopwords     中文停用词表
en_stopwords     英文停用词表
hit_stopwords    哈工大停用词表
scu_stopwords    四川大学机器智能实验室停用词库

"""


stopwords = set()

file_path = "txt/cn_stopwords.txt"  # 替换成您的停用词表文件路径

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip()
            stopwords.add(word)
except UnicodeDecodeError:
    # 如果使用 UTF-8 编码报错，尝试使用 GBK 编码打开文件
    with open(file_path, "r", encoding="gbk") as file:
        for line in file:
            word = line.strip()
            stopwords.add(word)

# 检查单词是否在停用词表中
word = "是"
if word in stopwords:
    print(f"'{word}' is a stopword.")
else:
    print(f"'{word}' is not a stopword.")
