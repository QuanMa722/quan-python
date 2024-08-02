# -*- coding: utf-8 -*-

from keyword import kwlist, softkwlist

count = 1
print("关键词")
for keyword in kwlist:
    print(count, keyword)
    count += 1

print()

count = 1
print("软文列表")
for keyword in softkwlist:
    print(count, keyword)
    count += 1

