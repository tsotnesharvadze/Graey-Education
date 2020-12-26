import time
from functools import wraps

def logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open(f'{func.__name__}_LOG', 'a') as file:
            file.writelines(f'ფუნქცია გამოიძახა არგუმენტებით: {args} {kwargs}\n')
        return func(*args, **kwargs)        
  
    return wrapper


def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        entry_time = time.time()
        res = func(*args, **kwargs)
        exuction_time = time.time() - entry_time
        print(f'{func.__name__}-ს მოუნდა {exuction_time} წამი')
        return res

    return wrapper


@logging
@time_it
def display(name: str, score: int):
    print(f'{name}ს აქვს {score} ქულა')

# # display = time_it(logging(display))

from typing import Any, Optional, Dict


def try_except(default: Optional[Any] = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return default
        return wrapper
    return decorator



@try_except(0)
def caluclate(x: int):
    return x / 0



if __name__ == '__main__':
    # print(
    # caluclate(3)
    # )

    display('Guido', 15)
