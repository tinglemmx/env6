# names = ['关羽', '张飞', '赵云', '马超', '黄忠']
# courses = ['语文', '数学', '英语']
# # 录入五个学生三门课程的成绩
# # 错误 - 参考http://pythontutor.com/visualize.html#mode=edit
# #scores = [[None] * len(courses)] * len(names)   这样建立的嵌套后面都是指针 第一个改了后面全改了
# scores = [[None] * len(courses) for _ in range(len(names))]
# for row, name in enumerate(names):
#     for col, course in enumerate(courses):
#         scores[row][col] = float(input(f'请输入{name}的{course}成绩: '))
#         print(scores)


# d = {'Java': "99", 'C': "99", 'C++': "99"}
# L = [k + '=' + v for k, v in d.items()]
#
# print(L)


print ([m + n for m in 'ABCD' for n in 'XYZ'])
