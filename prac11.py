import time
from functools import lru_cache


@lru_cache(maxsize=1)
def fun(n):
    time.sleep(n)
    return n


if __name__=='__main__':
    print("function are running....")
    fun(3)
    print("function are running again....")
    fun(3)
    print("function are running three times...")
    fun(3)
    print("function are running three times...")