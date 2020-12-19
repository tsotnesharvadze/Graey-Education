'''
x = 555555555555555


def my_func():
    global y
    y = 555555555555555
    z = 6

    print(id(y), id(z))

my_func()
print(id(x))
'''
import time
from typing import Iterable

from django.db import transaction


def my_upper(s):
    new = ''
    for i in s:
        if 'a' <= i <= 'z':
            i = chr(ord(i) - 32)
        new += i
    return new

# cotne = 'cotne' if my_upper else 'sharvadze'

# cotne = 'sharvadze'
# if my_upper:
#     cotne = 'cotne'
#
#
# print(cotne)

# a = ?()

# print(a(1)(2)(3)(4))

# 'sad{x}asdad{y}'.format(x=1, y=4)
# a= 9
# f'sadsad{2323}sadsadsa{a}' -> 'sadsad2323sadsadsa9'

a = '''def j():
    print('jjjj')
    return 0
stock = 10

def a():
    global stock
    try:
        stock -= 1
        return stock
    finally:
        stock +=1
b = a()

print(b)
print(stock)'''

# print(a)

# def my_sum(l: Iterable):
#     return sum(l)
# print(my_sum(range(1,4)))
# print(sum([1,2,3,5,56]))
#
#
# with open('cotne.txt', 'w') as cotne_txt:
#     print(cotne_txt.writelines(['a', 'b']))
#
#
#
# try:
#     import sadadad
#     [][6]
#
# except (IndexError, StopIteration) as E:
#     print('index error', E)
# except Exception as e:
#     print(e)
