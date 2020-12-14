# Lambda functions, უსახელო ფუნქციები

# data = [1, 2, 3]  my_map(square, data) -> [1, 4, 9]

# STATGE_MANAGMENT = {
#     '+': lambda x,y: x+y,
#     '-': lambda x,y: x-y
# }

# print(STATGE_MANAGMENT['+'](3, 4))

# def my_map(func, data):
#     for i in data:
#         yield func(i)

# print(
#     list(my_map(lambda x: x**3, [1, 2, 3]))
# )
# from typing import Callable


# def my_func(tag: str) -> Callable:
#     def second_func(data: str):
#         print(f'<{tag}> {data} </{tag}>')

#     return second_func


# print_h1 = my_func('h1')
# print_h1('data')

# print_h2 = my_func('h2')
# print_h2('Welcome to our site')
from typing import Callable

def my_decorator(func: Callable) -> Callable:
    def wrapper():
        print('შემოვიდა ვრაპპერ-ში')
        return func()
    return wrapper

@my_decorator
def display():
    print('Display MSG')


# display = my_decorator(display)
display()




# print(
#     list(map(square, [1, 2, 3]))
# )
# # args, kwargs

# def my_print(*args, **kwargs):
#     print(kwargs)
#     print(args, type(args))
#     for i in args:
#         print(i, end=' ')
#     print()


# data = ('a', 'b', 's', 's', 3)
# print(*data)
# my_print('a', 'b', 's', 's', 3, a=3, b=4)

# a = {
#     'a': "A"
# }

# b = {
#     'a': 3,
#     'b': "B"
# }

# d = {1: a, 2: b}

# c = {
#     **a, **b
# }

# c = a | b

# dict(**b) # dict(a=3, b="B")


# print(d)

# print(c)