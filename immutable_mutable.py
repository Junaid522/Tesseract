# y = 0
# x = 10
# x = y
#
# l = [1, 8]
# l = l.pop(1)
#
# print(id(x) == id(y))
# print(id(y) == id(10))
# print(id(l) == id(l))a

# def abc(e,bb=[]):
#
#   bb.append(e)
#
#   return bb
#
# print (abc(2))
#
# print(abc(3))
#
# print(abc(2))
#
# print(abc(2,[]))

# s = range(10) # it creates list of 10 elements that is mutable
# print(type(s))
#
# xrange = range
# ss = xrange(10) # it creates one element at one time in memory and its better than range because it uses generators and yeilds
#
# print(type(ss))


# class A:
#
#     def whereiam(self):
#
#         print("I am in A")
#
#
# class B(A):
#
#     def whereiam(self):
#
#         print("I am in B")
#
#
# class C(A):
#
#     def whereiam(self):
#
#         print("I am in C")
#
#
# class D(B, C):
#
#     def whereiam(self):
#
#         print("I am in D")
#
#
# d = D()
# print(D.mro())
# d.whereiam()

import random


def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield i
    # returns a 7th number between 1 and 15
    yield 15


for random_number in lottery():
    print("And the next number is... %d!" %(random_number))