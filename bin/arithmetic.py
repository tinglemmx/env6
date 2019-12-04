#!/usr/bin/env python
# _*_ coding: utf-8 _*_

# import numpy as np
# import copy
# from time import time, sleep
#
# def select_sort(origin_items, comp=lambda x, y: x < y):
#     """简单选择排序"""
#     items = copy.deepcopy(origin_items)
#     for i in range(len(items) - 1):
#         min_index = i
#         for j in range(i + 1, len(items)):
#             if comp(items[j], items[min_index]):
#                 min_index = j
#         items[i], items[min_index] = items[min_index], items[i]
#     return items
#
# def print_with_time(list):
#     start = time()
#     print(select_sort(list))
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))
#
# def main():
#     test_list = np.random.randint(10,20,size=10)
#     print(test_list)
#     print_with_time(test_list)
#     print(test_list)
#
# if __name__ == '__main__':
#     main()

# ================================================
#穷举法

# 公鸡5元一只 母鸡3元一只 小鸡1元三只
# 用100元买100只鸡 问公鸡/母鸡/小鸡各多少只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
            print(x, y, z)

# A、B、C、D、E五人在某天夜里合伙捕鱼 最后疲惫不堪各自睡觉
# 第二天A第一个醒来 他将鱼分为5份 扔掉多余的1条 拿走自己的一份
# B第二个醒来 也将鱼分为5份 扔掉多余的1条 拿走自己的一份
# 然后C、D、E依次醒来也按同样的方式分鱼 问他们至少捕了多少条鱼
fish = 6
while True:
    total = fish
    enough = True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(fish)
        break
    fish += 5