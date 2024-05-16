# -*- coding: utf-8 -*-

from keyword import kwlist, softkwlist

count = 1
print("the keyword")
for keyword in kwlist:
    print(f"{count}: {keyword}")
    count += 1

print()

count = 1
print("the softkwlist")
for keyword in softkwlist:
    print(f"{count}: {keyword}")
    count += 1
