from my_logging import time_it
from functools import lru_cache


@lru_cache()
def fibo(n: int) -> int:
    if n <= 1:
        return 1
    return fibo(n-1) + fibo(n-2)

