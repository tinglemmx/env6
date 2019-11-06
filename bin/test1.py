# def main():
#     num = int(input('Number of rows: '))
#     yh = [[]] * num
#     yhformat = []
#
#     for row in range(len(yh)):
#         yhstr = ''
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] = 1
#                 yhstr += '{0}\t'.format(str(yh[row][col]))
#             else:
#                 yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
#                 yhstr += '{0}\t'.format(str(yh[row][col]))
#         print(yhstr)
#         yhformat.append(yhstr)
#
#     print(yhformat)
#
#     for prow in yhformat:
#         print('{:^50}'.format(prow))
#
#
# if __name__ == '__main__':
#     main()

# result1 = []
# width = 5
# result = ['a','b','c','d','e']
# for i in result:
#     result1.append('{0:^{1}}'.format(str(i), width))
#
# column = 20
# print('{0:^{1}}'.format(''.join(result1), column))

#
# from math import sqrt
#
#
# class Point(object):
#
#     def __init__(self, x=0, y=0):
#         """初始化方法
#
#         :param x: 横坐标
#         :param y: 纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_to(self, x, y):
#         """移动到指定位置
#
#         :param x: 新的横坐标
#         "param y: 新的纵坐标
#         """
#         self.x = x
#         self.y = y
#
#     def move_by(self, dx, dy):
#         """移动指定的增量
#
#         :param dx: 横坐标的增量
#         "param dy: 纵坐标的增量
#         """
#         self.x += dx
#         self.y += dy
#
#     def distance_to(self, other):
#         """计算与另一个点的距离
#
#         :param other: 另一个点
#         """
#         dx = self.x - other.x
#         dy = self.y - other.y
#         return sqrt(dx ** 2 + dy ** 2)
#
#     def __str__(self):
#         return '(%s, %s)' % (str(self.x), str(self.y))
#
#
# def main():
#     p1 = Point(3, 5)
#     p2 = Point()
#     print(p1)
#     print(p2)
#     p2.move_by(-1, 2)
#     print(p2)
#     print(p1.distance_to(p2))
#
#
# if __name__ == '__main__':
#     main()

#
# class Dog(object):
#     def __init__(self):
#         print("----init方法-----")
#
#     def __del__(self):
#         print("----del方法-----")
#
#     def __str__(self):
#         print("----str方法-----")
#         return "对象的描述信息"
#
#     def __new__(cls):#cls此时是Dog指向的那个类对象
#
#         #print(id(cls))
#
#         print("----new方法-----")
#         return object.__new__(cls)
#
#
# #print(id(Dog))
#
# xtq = Dog()
#
#
# class Dog(object):
#     def __init__(self,name):
#         self.name = abs(name)
#         print("----init方法-----")
#         print(self.name)
#
#     def __del__(self):
#         print("----del方法-----")
#
#     def __str__(self):
#         print("----str方法-----")
#         return "对象的描述信息"
#
#     def __new__(cls,name):#cls此时是Dog指向的那个类对象
#
#         #print(id(cls))
#
#         print("----new方法-----")
#         return object.__new__(cls)
#
#
# #print(id(Dog))
#
# xtq = Dog(15.00)


#
# class Person(object):
#
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     # 访问器 - getter方法
#     @property
#     def name(self):
#         return self._name
#
#     # 访问器 - getter方法
#     @property
#     def age(self):
#         return self._age
#
#     # 修改器 - setter方法
#     @age.setter
#     def age(self, age):
#         self._age = age
#
#     def play(self):
#         if self._age <= 16:
#             print('%s正在玩飞行棋.' % self._name)
#         else:
#             print('%s正在玩斗地主.' % self._name)
#
#
# def main():
#     person = Person('王大锤', 12)
#     person.play()
#     person.age = 22
#     person.play()
#     # person.name = '白元芳'  # AttributeError: can't set attribute
#
#
# if __name__ == '__main__':
#     main()



#
# from math import sqrt
#
#
# class Triangle(object):
#
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and b + c > a and a + c > b
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#
#     def area(self):
#         half = self.perimeter() / 2
#         return sqrt(half * (half - self._a) *
#                     (half - self._b) * (half - self._c))
#
#
# def main():
#     a, b, c = 3, 1, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
#         # print(Triangle.perimeter(t))
#         print(t.area())
#         # print(Triangle.area(t))
#     else:
#         print('无法构成三角形.')
#
#
# if __name__ == '__main__':
#     main()



from abc import ABCMeta, abstractmethod
class Pet(object, metaclass=ABCMeta):
    """宠物"""
    def __init__(self, nickname):
        self._nickname = nickname
    @abstractmethod
    def make_voice(self):
        """发出声音"""
        pass
class Dog(Pet):
    """狗"""
    def make_voice(self):
        print('%s: 汪汪汪...' % self._nickname)
class Cat(Pet):
    """猫"""
    def make_voice(self):
        print('%s: 喵...喵...' % self._nickname)
def main():
    pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
    for pet in pets:
        pet.make_voice()
if __name__ == '__main__':
    main()
