#!/usr/bin/python
#coding=utf-8
# __author__ = 'cy'
#输出杨辉三角数值表 ,金字塔形
def triangle(num):
#初始表值为[1]
    triangle=[[1]]
#添加i个值([1])至triangle表,eg:[1]*3,triangle=[[1], [1], [1]]
    for i in range(2, num+1):
        triangle.append([1]*i)
#改变triangle表的值,eg:
#当num=5时，i取5，j取3
#triangle[4][1] = triangle[3][1]+triangle[3][0]
#triangle[4][2] = triangle[3][2]+triangle[3][1]
#triangle[4][3] = triangle[3][3]+triangle[3][2]
#相当于triangle表的第4位的值(这里的值为一个表)的第1,2,3位值等于第3位的值(这里的值也是一个表)的第1,2,3位值和0,1,2的值分别相加(即错位相加)。
        for j in range(1, i-1):
            triangle[i-1][j] = triangle[i-2][j]+triangle[i-2][j-1]
    return triangle
#格式化输出(输出的是一个表)
def printtriangle(triangle, width):
#列宽
    column = len(triangle[-1])*width
    for sublist in triangle:
        result = []
        for contents in sublist:
#控制间距
            result.append('{0:^{1}}'.format(str(contents), width))
#控制缩进，{0:^{1}}：空格在两边补齐空位‘^’居中对齐，‘:’号后面带填充的字符
        print('{0:^{1}}'.format(''.join(result), column)) #''.join(result)就是用''里的东西把resut的字母连起来
#启动函数
if __name__ == '__main__':
#输入整数
    num = int(input('How many rows do you want:'))
#打印信息
    print ("The triangle rows as follows:")
    triangle = triangle(num)
#列宽
    width = len(str(triangle[-1][len(triangle[-1])//2]))+3
    printtriangle(triangle, width)

