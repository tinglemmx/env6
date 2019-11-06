#!/usr/bin/env python
# _*_ coding: utf-8 _*_


"""
my_sum = 0
for i in range(1, 101):
    my_sum += i
print(my_sum)



#+=测试
my_num = 1

my_num += my_num
print(my_num)

"""
#
# import random
#
# answer = random.randint(1,100)
# counter = 0
# while True:
#     counter +=1
#     number = int(input('请输入：'))
#     if number < answer:
#         print('小')
#     elif number > answer:
#         print ('大')
#     else:
#         print('对')
#         break
# print('你总共猜了%d次'% counter)
#
# =========================================
# #九九乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d' % (i, j, i * j), end='\t')
#     print()   #这个是用来换行的
# =============================================
# a = 10
# b = 20
# a,b = b,a   #将a，b的值呼唤
# print(a)
# print(b)
# ==========================================
# 生成斐波那契数列的前20个数。
# a = 1
# b = 1
# print(a)
# print(b)
# for i in range(20):
#     c = a + b
#     print(c)
#     a = b
#     b = c
#
# ==========================================
#
# #找出10000以内的完美数
# for i in range(2,10001):
#     q = 0
#     for j in range(1,i):
#         if (i % j)== 0:
#             q += j
#     if i==q:
#         print(i)
# =====================================
# 输出100以内所有的素数
# for i in range (1,100):
#     k = int(pow(i,1/2))
#     for j in range (2,k+2):
#         if i % j == 0:
#             break
#         else:
#             print(i)
#             break
#
# def foo():
#     print('hello, world!')
#
#
# def foo():
#     print('goodbye, world!')
#
#
# # 下面的代码会输出什么呢？
# foo()

# def is_prime(num):
# #     """判断一个数是不是素数"""
# #     for factor in range(2, num):
# #         if num % factor == 0:
# #             return False
# #     return True if num != 1 else False
# #
# # print(is_prime(3))


# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
# arg = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*arg, **kw)


# def foo():
#     b = 'hello'
#
#     # Python中可以在函数内部再定义函数
#     def bar():
#         c = True
#         print(a)
#         print(b)
#         print(c)
#
#     bar()
#     # print(c)  # NameError: name 'c' is not defined
#
#
# if __name__ == '__main__':
#     a = 100
#     # print(b)  # NameError: name 'b' is not defined
#     foo()

# def foo():
#     a = 200
#     print(a)  # 200
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 100

#
# def foo():
#     global a
#     a = 200
#     print(a)  # 200
#
#
# if __name__ == '__main__':
#     a = 100
#     foo()
#     print(a)  # 200


# s1 = '\'hello, world!\''
# s2 = '\n\\hello, world!\\\n'
# print(s1, s2, end='')
#
# s1 = r'\'hello, world!\''
# s2 = r'\n\\hello, world!\\\n'
# print(s1, s2)
# print('wo' not in s2)
# print(s2[::-1])
# print(s2[1:5])
# print(s2[1:5:2])
# print(s2[:])
# print(s2[:-1])
# print(s2[:])

#
# str1 = ''
# s = 'abcdefghijklmnopqrstuvwxyz'
# for i in  range(0,len(s)+1,4):
#     str1 += s[i:i+4]+' '
# print(str1)
# print(str1.title())
# print(str1.find('c'))
#
# str1 = 'hello, world!'
# print(str1.find('or'))
# print(str1.find('o'))
# print(str1.find('r'))
# print(str1.center(50, '*'))
#
# str3 = '  jackfrued@126.com '
# print(str3)
# # 获得字符串修剪左右两侧空格之后的拷贝
# print(str3.strip())
# print(str3.is)


#
# a = 5
# b = 6
# print('%d * %d = %d' %(a,b,a*b))
# print ('{0} + {1} = {2}'.format(a,b,a*b))
# print (f'{a} * {b} = {a * b}')

# import datetime
#
#
# now=datetime.datetime.now()
# print(type(now))
# print ('{0:%Y-%m-%d %X}'.format(now))


# list1 = [1, 3, 5, 7, 100]
# for index in range(len(list1)):
#     print(list1[index])
# # 通过for循环遍历列表元素
# for elem in list1:
#     print(elem)
# # 通过enumerate函数处理列表之后再遍历可以同时获得元素索引和值
# for index, elem in enumerate(list1):
#     print(index, elem)


# list1 = [1, 3, 5, 7, 100]
# # 添加元素
# list1.append(200)
# list1.insert(1, 400)
# # 合并两个列表
# # list1.extend([1000, 2000])
# list1 += [1000, 2000]
# print(list1) # [1, 400, 3, 5, 7, 100, 200, 1000, 2000]
# print(len(list1)) # 9
# # 先通过成员运算判断元素是否在列表中，如果存在就删除该元素
# if 3 in list1:
# 	list1.remove(3)
# if 1234 in list1:
#     list1.remove(1234)
# print(list1) # [1, 400, 5, 7, 100, 200, 1000, 2000]
# # 从指定的位置删除元素
# list1.pop(0)
# print(list1)
# list1.pop(len(list1) - 1)
# print(list1) # [400, 5, 7, 100, 200, 1000]
# # 清空列表元素
# list1.clear()
# print(list1) # []


# set2 = set(range(1, 10))
# set3 = set((1, 2, 3, 3, 2, 1))
# print(set2, set3)
# set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}  #放一行写
# print(set4)
#
# set1 = {'a', 'b', 'c','d', 'e'}
# set1.add(4)
# set1.add(5)
# set1.update([11,12])
# print(set1)
# set1.discard('a')
# print(set1)
# set1.pop()
# print(set1)
# set1.pop()
# print(set1)
# set1.add(14)
# set1.add(15)
# set1.update([111,112])
# print(set1)



# set1 = {x for x in range(1,10)}
# # set2 = {y for y in range(1,20,2)}
# # set3 = {z for z in range(1,10) if z%2==0}
# #
# # print(set1,set2,sep='\n')
# #
# # print ("set1 & set2",set1 & set2)
# # print ('set1 | set2',set1 | set2)
# # print ('set1 - set2',set1 - set2)
# # print ('set2 - set1',set2 - set1)
# # print('set1 ^ set2',set1 ^ set2)
# # print ('set1 <= set2',set1 <= set2)
# # print ('set1 >= set2',set1 >= set2)
# # print ('set3=',set3)
# # print ('set3 <= set1',set3 <= set1)


# 创建字典的字面量语法
scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
# print(scores)
# # 创建字典的构造器语法
# items1 = dict(one=1, two=2, three=3, four=4)
# # 通过zip函数将两个序列压成字典
# items2 = dict(zip(['a', 'b', 'c'], '123'))
# # 创建字典的推导式语法
# items3 = {num: num ** 2 for num in range(1, 10)}
# print(items1, items2, items3)
# # 通过键可以获取字典中对应的值
# print(scores['骆昊'])
# print(scores['狄仁杰'])
# # 对字典中所有键值对进行遍历
# for key in scores:
#     print(f'{key}: {scores[key]}')
# # 更新字典中的元素
# scores['白元芳'] = 65
# scores['诸葛王朗'] = 71
# scores.update(冷面=67, 方启鹤=85)
# print(scores)
# if '武则天' in scores:
# #      print(scores['武则天'])
# print(scores.get('武则天'))
# # # get方法也是通过键获取对应的值但是可以设置默认值
# # print(scores.get('武则天', 60))
# # # 删除字典中的元素
# print(scores.popitem())
# print(scores.popitem())
# print(scores.pop('骆昊', 100))
# # 清空字典
# scores.clear()
# print(scores)



#


