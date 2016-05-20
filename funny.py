#coding:utf-8
from time import time, sleep
##不重复的三位数

# start = time()
# count = 0
# for i in range(100, 1000):
#     str_i = str(i)
#     a = str_i[0]
#     b = str_i[1]
#     c = str_i[2]
#     if a != b and a != c and b != c:
#         # print(i)
#         count += 1
# print("Count: %s"%count)
# print(time() - start)

##水仙花数

start = time()
count = 0
for i in range(100, 1000):
    str_i = str(i)
    a = int(str_i[0])
    b = int(str_i[1])
    c = int(str_i[2])
    if (a**3 + b**3 + c**3) == i:
        print(i)
        count += 1
print("Count: %s"%count)
print(time() - start)