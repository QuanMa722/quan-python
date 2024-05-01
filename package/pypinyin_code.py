# -*- coding: utf-8 -*-

from pypinyin import pinyin, Style

# 将汉字转换为拼音
hanzi = input("请输入汉字:")
pinyin_list = pinyin(hanzi, style=Style.NORMAL)

# 输出拼音结果
pinyin_str = ''.join([item[0] for item in pinyin_list])
print("拼音结果:", pinyin_str)
