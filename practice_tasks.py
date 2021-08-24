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
# print(d.whereiam())
# print(D.mro())
#
# D().whereiam()


## pass by reference
# def abc(e,bb=[]):
#   bb.append(e)
#   return bb
#
# print(abc(2))
# print(abc(3))
# print(abc(2))
# print(abc(2,[]))

## lambda functions
# def create_multipliers():
#     return [lambda x : i * x for i in range(5)]

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

# def lottery():
#
#     # returns 6 numbers between 1 and 40
#     for i in range(6):
#
#         yield i
#     # returns a 7th number between 1 and 15
#
#     yield 15
#     yield 20
#
#
# for random_number in lottery():
#     print("And the next number is... %d!" %(random_number))
# from functools import reduce
#
# number = 2345
#
# result = 1
#
# while number > 0:
#     result *= int(number % 10)
#     number = int(number / 10)
#
# print(result)
#
#
# str_var = 'teeth'
# str_list = []
# for s in str_var:
#     if s in str_list:
#         str_list.remove(s)
#     str_list.append(s)
#
# print("".join(str_list))
#
#
# li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# final_list = list(filter(lambda x: x % 2 != 0, li))
# print(final_list)
#
# final_list = list(map(lambda x: x*2, li))
# print(final_list)
#
# summation = reduce(lambda x, y: x + y, li)
#
# print(summation)
#
#
# def uppercase_decorator(function):
#     def wrapper():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#
#     return wrapper
#
#
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
# print(say_hi())
#
#
# def split_string(function):
#     def wrapper():
#         func = function()
#         splitted_string = func.split()
#         return splitted_string
#
#     return wrapper
#
#
# @split_string
# @uppercase_decorator
# def say_hi():
#     return 'hello there'
#
#
# print(say_hi())
#
#
# class A(object):
#     def foo(self, x):
#         print("executing foo(%s, %s)" % (self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo(%s, %s)" % (cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)
#
# a = A()
# print(a.foo(3))
#
# print(a.class_foo(4))
#
# print(a.static_foo(6))


# def isPrime(n, i=2):
#     if n <= 2:
#         return True if n == 2 else False
#
#     elif n - (i * (n//i)) == 0:
#         return False
#
#     elif i*i > n:
#         return True
#
#     return isPrime(n, i+1)


# print(isPrime(5))

# print(isPrime(6))

# print(isPrime(9))


# a = 'abc'
# b=a
# print(id(a) == id(b))
#
# def is_possible(n, m, k):
#     brick5 = k // n
#     brick1 = k - brick5 * 5
#     print(brick5)
#     print(brick1)
#
#     if brick5 * 5 + brick1 == k:
#         return True
#     return False


# print(is_possible(5, 1, 13))


# def gen():
#     l = range(6)
#     for i in l:
#         yield i * i
#
#
# for i in gen():
#     print(i)


# x = [{'a': 1}, {'b': 2}, {'c': 3}]
# hell = [i[list(i.keys())[0]] for i in x]
#
# print(hell)


# def string_uppercase(function):
#     def funcwrapper():
#         func = function()
#         upper_case = func.upper()
#         return upper_case
#
#
# @string_uppercase
# def string_maker():
#     print('kilometer')
#
# string_maker()


# l = [x for x in range(5)]
# print(l)

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
#
# new_list = [x.__contains__('a') for x in fruits]
#
# palindrome = 'wasamhdadbqkokhfaafl'

# def find_plaindromes():
#     new_list = []
#     for i in palindrome:
#

# def foo(n):
#
#     return n
#
# fun = foo(3)
# res = fun(5)
# 5*3
# 15


# def is_palindrome(str):
#     new_str = str[len(str)/2]


# print(new_list)


