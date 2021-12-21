# # s = range(10) # it creates list of 10 elements that is mutable
# # print type(s)
# #
# # ss = xrange(10) # it creates one element at one time in memory and its better than range because it uses generators and yeilds
# # print type(ss)
# #
# #
# # class A:
# #
# #     def whereiam(self):
# #
# #         print("I am in A")
# #
# # class B(A):
# #     pass
# #     # def whereiam(self):
# #     #
# #     #     print("I am in B")
# #
# # class C(A):
# #     pass
# #     # def whereiam(self):
# #     #
# #     #     print("I am in C")
# #
# # class D(B, C):
# #     pass
# #     # def whereiam(self):
# #     #
# #     #     print("I am in D")
# #
#
# #
# # d = D()
# # print(d.whereiam())
# # print(D.mro())
# #
# # D().whereiam()
#
#
# ## pass by reference
# # def abc(e,bb=[]):
# #   bb.append(e)
# #   return bb
# #
# # print(abc(2))
# # print(abc(3))
# # print(abc(2))
# # print(abc(2,[]))
#
# ## lambda functions
# # def create_multipliers():
# #     return [lambda x : i * x for i in range(5)]
#
# # for multiplier in create_multipliers():
# #     print(multiplier(2))
# #
#
# # li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# # final_list = list(filter(lambda x: (x%2 == 0) , li))
# # print(final_list)
#
#
# # objects having __hash__()
# # ll = [2,4,]
# # print dir(ll)
# # print ll.__hash__
# #
# # ss = " this is pakistan"
# #
# # print dir(ss)
# # print ss.__hash__()
#
#
# # late binding closures
# # from functools import partial
# # from operator import mul
# #
# # def create_multipliers():
# #     return [partial(mul, i) for i in range(5)]
# #
# # print create_multipliers()
# import queue
# import random
#
# # def lottery():
# #
# #     # returns 6 numbers between 1 and 40
# #     for i in range(6):
# #
# #         yield i
# #     # returns a 7th number between 1 and 15
# #
# #     yield 15
# #     yield 20
# #
# #
# # for random_number in lottery():
# #     print("And the next number is... %d!" %(random_number))
# # from functools import reduce
# #
# # number = 2345
# #
# # result = 1
# #
# # while number > 0:
# #     result *= int(number % 10)
# #     number = int(number / 10)
# #
# # print(result)
# #
# #
# # str_var = 'teeth'
# # str_list = []
# # for s in str_var:
# #     if s in str_list:
# #         str_list.remove(s)
# #     str_list.append(s)
# #
# # print("".join(str_list))
# #
# #
# # li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# # final_list = list(filter(lambda x: x % 2 != 0, li))
# # print(final_list)
# #
# # final_list = list(map(lambda x: x*2, li))
# # print(final_list)
# #
# # summation = reduce(lambda x, y: x + y, li)
# #
# # print(summation)
# #
# #
# # def uppercase_decorator(function):
# #     def wrapper():
# #         func = function()
# #         make_uppercase = func.upper()
# #         return make_uppercase
# #
# #     return wrapper
# #
# #
# # @uppercase_decorator
# # def say_hi():
# #     return 'hello there'
# #
# # print(say_hi())
# #
# #
# # def split_string(function):
# #     def wrapper():
# #         func = function()
# #         splitted_string = func.split()
# #         return splitted_string
# #
# #     return wrapper
# #
# #
# # @split_string
# # @uppercase_decorator
# # def say_hi():
# #     return 'hello there'
# #
# #
# # print(say_hi())
# #
# #
# # class A(object):
# #     def foo(self, x):
# #         print("executing foo(%s, %s)" % (self, x))
# #
# #     @classmethod
# #     def class_foo(cls, x):
# #         print("executing class_foo(%s, %s)" % (cls, x))
# #
# #     @staticmethod
# #     def static_foo(x):
# #         print("executing static_foo(%s)" % x)
# #
# # a = A()
# # print(a.foo(3))
# #
# # print(a.class_foo(4))
# #
# # print(a.static_foo(6))
#
#
# # def isPrime(n, i=2):
# #     if n <= 2:
# #         return True if n == 2 else False
# #
# #     elif n - (i * (n//i)) == 0:
# #         return False
# #
# #     elif i*i > n:
# #         return True
# #
# #     return isPrime(n, i+1)
#
#
# # print(isPrime(5))
#
# # print(isPrime(6))
#
# # print(isPrime(9))
#
#
# # a = 'abc'
# # b=a
# # print(id(a) == id(b))
# #
# # def is_possible(n, m, k):
# #     brick5 = k // n
# #     brick1 = k - brick5 * 5
# #     print(brick5)
# #     print(brick1)
# #
# #     if brick5 * 5 + brick1 == k:
# #         return True
# #     return False
#
#
# # print(is_possible(5, 1, 13))
#
#
# # def gen():
# #     l = range(6)
# #     for i in l:
# #         yield i * i
# #
# #
# # for i in gen():
# #     print(i)
#
#
# # x = [{'a': 1}, {'b': 2}, {'c': 3}]
# # hell = [i[list(i.keys())[0]] for i in x]
# #
# # print(hell)
#
#
# # def string_uppercase(function):
# #     def funcwrapper():
# #         func = function()
# #         upper_case = func.upper()
# #         return upper_case
# #
# #
# # @string_uppercase
# # def string_maker():
# #     print('kilometer')
# #
# # string_maker()
#
#
# # l = [x for x in range(5)]
# # print(l)
#
# # fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# #
# # new_list = [x.__contains__('a') for x in fruits]
# #
# # palindrome = 'wasamhdadbqkokhfaafl'
#
# # def find_plaindromes():
# #     new_list = []
# #     for i in palindrome:
# #
#
# # def foo(n):
# #
# #     return n
# #
# # fun = foo(3)
# # res = fun(5)
# # 5*3
# # 15
#
#
# # def is_palindrome(str):
# #     new_str = str[len(str)/2]
#
#
# # print(new_list)
#
#
# # # Expand in both directions of `low` and `high` to find all palindromes
# # def expand(s, low, high, palindromes):
# #     # run till `s[low.high]` is not a palindrome
# #     while low >= 0 and high < len(s) and s[low] == s[high]:
# #         # push all palindromes into a set
# #         palindromes.add(s[low: high + 1])
# #
# #         # Expand in both directions
# #         low = low - 1
# #         high = high + 1
# #
# #
# # # Function to find all unique palindromic substrings of a given string
# # def findPalindromicSubstrings(s):
# #     # create an empty set to store all unique palindromic substrings
# #     palindromes = set()
# #
# #     for i in range(len(s)):
# #         # find all odd length palindrome with `s[i]` as a midpoint
# #         expand(s, i, i, palindromes)
# #
# #         # find all even length palindrome with `s[i]` and `s[i+1]`
# #         # as its midpoints
# #         expand(s, i, i + 1, palindromes)
# #
# #     # print all unique palindromic substrings
# #     print(palindromes, end='')
# #
# #
# # findPalindromicSubstrings('google')
#
#
# import json
# import threading
# import time
# from time import sleep
# import requests
# import urlopen as urlopen
# from bs4 import BeautifulSoup
#
#
# def parse(u):
#     title = '-'
#     submit_by = '-'
#     description = '-'
#     calories = 0
#     ingredients = []
#     rec = {}
#     try:
#         r = requests.get(u, headers=headers)
#         if r.status_code == 200:
#             html = r.text
#             soup = BeautifulSoup(html, 'lxml')
#             # title
#             title_section = soup.select('.recipe-summary__h1')
#             # submitter
#             submitter_section = soup.select('.submitter__name')
#             # description
#             description_section = soup.select('.submitter__description')
#             # ingredients
#             ingredients_section = soup.select('.recipe-ingred_txt')
#             # calories
#             calories_section = soup.select('.calorie-count')
#             if calories_section:
#                 calories = calories_section[0].text.replace('cals', '').strip()
#         if ingredients_section:
#             for ingredient in ingredients_section:
#                 ingredient_text = ingredient.text.strip()
#                 if 'Add all ingredients to list' not in ingredient_text and ingredient_text != '':
#                     ingredients.append({'step': ingredient.text.strip()})
#         if description_section:
#             description = description_section[0].text.strip().replace('"', '')
#         if submitter_section:
#             submit_by = submitter_section[0].text.strip()
#         if title_section:
#             title = title_section[0].text
#         rec = {'title': title, 'submitter': submit_by, 'description': description, 'calories': calories,
#                'ingredients': ingredients}
#     except Exception as ex:
#         print('Exception while parsing')
#         print(str(ex))
#     finally:
#         return json.dumps(rec)
#
#
# if __name__ == '__main__':
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
#         'Pragma': 'no-cache'
#     }
#     url = 'https://www.allrecipes.com/recipes/96/salad/'
#     r = requests.get(url, headers=headers)
#     if r.status_code == 200:
#         html = r.text
#         soup = BeautifulSoup(html, 'lxml')
#         links = soup.select('.fixed-recipe-card__h3 a')
#         for link in links:
#             sleep(2)
#             result = parse(link['href'])
#             print(result)
#             print('=================================')
#
#
# #x = 'cat'
# # def f():
# #     x = 'bird'
# #     def g():
# #         x = 'dog'
# #         y = 'fish'
# #         print(x)
# #     g()
# # f()
# #
# #
# # M = [[1,2,3],
# #      [4,5,6],
# #      [7,8,9]]
# #
# # MT = [[row[i] for row in M] for i in range(3)]
# #
# # print(MT)
# #
# # print(type(enumerate('python')))
# #
# #
# # print("I need %s, %s" % ("bread", "milk"))
# #
# # values = ["bread", "milk"]
# # item_1 = "t "
# # item_2 = "i "
# # # greeting = (' ').join(values)
# # greeting = f"I need {item_1} {item_2}"
# # print(greeting)
# #
# #
# # def f(x, y,z):
# #     return x + y + z
# #
# # # f(1, 2)
# #
# # a = 0
# # for i in range(10):
# #     if i == 2:
# #         pass
# #     else:
# #         a = i
# #
# # print(a)
# #
# # x = ["1", "2", "15", "-7", "300"]
# # y = sorted(x)
# # print(y)
# #
# # def recursive_string_reverse(strr):
# #     if len(strr) <= 1:
# #         return strr
# #     first_char = strr[0]
# #     last_char = strr[1:len(strr)]
# #     return
#
# q = queue.Queue()
# for i in [3, 2, 1]:
#     def f():
#         time.sleep(i)
#         q.put(i)
#     threading.Thread(target=f).start()
# print(q.get())
#
# def b(sl):
#     r = {}
#     for sent in sl:
#         b = r
#         for w in sent.split(' '):
#             if not b.get(w):
#                 b[w] = {}
#             b = b[w]
#
#
#     return r
#
# print(b(["Hello world!", "Hello There"]))
#
# def func(a, b):
#     a += 1
#     b.append(1)
#
# a, b = 0, []
# func(a, b)
# print(a, b)
#
# def dbI(t):
#     i = 0
#     while i < len(t):
#         if len(t[i]) == 0:
#             del t[i]
#         i += 1
#
# names = ["as", "", "mac", "", "ti"]
# print(dbI(names))
#
# words = ["Hello", "World"]
# for i, word in enumerate(words):
#     word.lower()
#     words[i] = word[::-1]
#
# print(words)
#
# def hpn(nums):
#     h_pos = False
#     h_neg = False
#     for n in nums:
#         h_pos = n > 0
#         h_neg = n < 0
#     return h_pos, h_neg
#
#
# print(hpn([0,1,2]))
# print(hpn([0,-1,-2]))
# print(hpn([-1,0,1]))
# print(hpn([]))


class Developer:
    def __init__(self):
        self.__seniority = 'Junior'
        self.skills = ''

    def display(self):
        print('Welcome to Turing with {seniority} developer with skill {skills}'.format(seniority=self.__seniority,
                                                                                        skills=self.skills))

class NodeJS(Developer):
    def __init__(self):
        super().__init__()
        self.__seniority = 'Senior'
        self.skills = 'NodeJS'


c =NodeJS()
c.display()


l = [1, 2, 3, 4]
m = map(lambda x: 2**x, l)
print(list(m))

# def inc(x):
#     return x+1
# print(list(map(inc, data)))

class Developer(object):
    def __init__(self, skills):
        self.skills = skills
    def __add__(self, other):
        skills = self.skills + other.skills
        return Developer(skills)
    def __str__(self):
        return "skills"

A =  Developer('NodeJS')
B =  Developer('Python')
print(A+B)

x = ['ab', 'cd']
print(list(map(lambda x: len(x),x)))

ap = 'abcd'
for i in range(len(ap)):
    ap[i].upper()
print(ap)

def skills(v, l=[]):
    l.append(v)
    return l

l1 = skills('NodeJs')
l2 = skills('Java', [])
l3 = skills('ReactJS')
print("%s", l1)
print("%s", l2)
print("%s", l3)

b = [sum(l[0:x+1]) for x in range(0, len(l))]
print(b)

# i = 'Welcome'
# def wel(i):
#     i = i + ', Welcome to Turing' return i

def isValid(self, s: str) -> bool:
    pair = dict(('()', '[]', '{}'))
    st = []
    for x in s:
        if x in '([{':
            st.append(x)
        elif len(st) == 0 or x != pair[st.pop()]:
            return False
    return len(st) == 0

