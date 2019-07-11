# s = range(10) # it creates list of 10 elements that is mutable
# print type(s)
#
# ss = xrange(10) # it creates one element at one time in memory and its better than range because it uses generators and yeilds
# print type(ss)
#
#
# class A:
#
#     def whereiam(self):
#
#         print("I am in A")
#
# class B(A):
#     pass
#     # def whereiam(self):
#     #
#     #     print("I am in B")
#
# class C(A):
#     pass
#     # def whereiam(self):
#     #
#     #     print("I am in C")
#
# class D(B, C):
#     pass
#     # def whereiam(self):
#     #
#     #     print("I am in D")
#

#
# d = D()
#
# print(D.mro())
#
# D().whereiam()


# pass by reference
# def abc(e,bb=[]):
#   bb.append(e)
#   return bb

# print abc(2)
# print abc(3)
# print abc(2
# print abc(2,[])

# lambda functions
# def create_multipliers():
#     return [lambda x : i * x for i in range(5)]
#
# for multiplier in create_multipliers():
#     print(multiplier(2))
#

# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: (x%2 == 0) , li))
# print(final_list)


# objects having __hash__()
# ll = [2,4,]
# print dir(ll)
# print ll.__hash__
#
# ss = " this is pakistan"
#
# print dir(ss)
# print ss.__hash__()


# late binding closures
# from functools import partial
# from operator import mul
#
# def create_multipliers():
#     return [partial(mul, i) for i in range(5)]
#
# print create_multipliers()


import random



def lottery():

    # returns 6 numbers between 1 and 40

    for i in range(6):

        yield i



    # returns a 7th number between 1 and 15

    yield 15



for random_number in lottery():

       print("And the next number is... %d!" %(random_number))