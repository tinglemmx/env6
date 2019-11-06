# =======================================
# IO 用try 来防止出错时程序奔溃
# =======================================
# def main():
#     f = None
#     try:
#         f = open('test.txt', 'r', encoding='utf-8')
#         print(f.read())
#     except FileNotFoundError:
#         print('无法打开指定的文件!')
#     except LookupError:
#         print('指定了未知的编码!')
#     except UnicodeDecodeError:
#         print('读取文件时解码错误!')
#     finally:
#         if f:
#             f.close()
#
#
# if __name__ == '__main__':
#     main()
# =======================================
# 逐行读取
# =======================================
# import time
#
#
# def main():
#     # 一次性读取整个文件内容
#     with open('test.txt', 'r', encoding='utf-8') as f:
#         print(f.read())
#
#     # 通过for-in循环逐行读取
#     with open('test.txt', mode='r') as f:
#         for line in f:
#             print(line, end='')
#             time.sleep(0.5)
#     print()
#
#     # 读取文件按行读取到列表中
#     with open('test.txt') as f:
#         lines = f.readlines()
#     print(lines)
#
#
# if __name__ == '__main__':
#     main()
# =======================================
# 写文件 如果文件没有就创建
# =======================================
#
# from math import sqrt
#
#
# def is_prime(n):
#     """判断素数的函数"""
#     assert n > 0
#     for factor in range(2, int(sqrt(n)) + 1):
#         if n % factor == 0:
#             return False
#     return True if n != 1 else False
#
#
# def main():
#     filenames = ('a.txt', 'b.txt', 'c.txt')
#     fs_list = []
#     try:
#         for filename in filenames:
#             fs_list.append(open(filename, 'a', encoding='utf-8'))
#         for number in range(1, 10000):
#             if is_prime(number):
#                 if number < 100:
#                     fs_list[0].write(str(number) + '\n')
#                 elif number < 1000:
#                     fs_list[1].write(str(number) + '\n')
#                 else:
#                     fs_list[2].write(str(number) + '\n')
#     except IOError as ex:
#         print(ex)
#         print('写文件时发生错误!')
#     finally:
#         for fs in fs_list:
#             fs.close()
#     print('操作完成!')
#
#
# if __name__ == '__main__':
#     main()

# =======================================
# 读写二进制文件 如果文件没有就创建，完成复制照片
# =======================================

# def main():
#     try:
#         with open('IMG_3911.JPG', 'rb') as fs1:
#             data = fs1.read()
#             print(type(data))  # <class 'bytes'>
#         with open('mc.jpg', 'wb') as fs2:
#             fs2.write(data)
#     except FileNotFoundError as e:
#         print('指定的文件无法打开.')
#     except IOError as e:
#         print('读写文件时出现错误.')
#     print('程序执行结束.')
#
#
# if __name__ == '__main__':
#     main()


# ==================================
# 读写JSON文件
# ==================================
# import json
# def main():
#     mydict = {
#         'name': '骆昊',
#         'age': 38,
#         'qq': 957658,
#         'friends': ['王大锤', '白元芳'],
#         'cars': [
#             {'brand': 'BYD', 'max_speed': 180},
#             {'brand': 'Audi', 'max_speed': 280},
#             {'brand': 'Benz', 'max_speed': 320}
#         ]
#     }
#     try:
#         with open('data.json', 'w', encoding='utf-8') as fs:
#             json.dump(mydict, fs)
#     except IOError as e:
#         print(e)
#     print('保存数据完成!')
# if __name__ == '__main__':
#     main()

#import requests
# import json
#
#
# def main():
# #    resp = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')由于调用天行的数据接口要钱的 我就用文件代替了
#     try:
#         with open('json_test_news.txt','r',encoding='utf-8') as f:
#             data_model = json.load(f)
#     except IOError as  ex:
#         print(ex)
#
#
#     for news in data_model['newslist']:
#         print(news['title'])

#
#
# if __name__ == '__main__':
#     main()