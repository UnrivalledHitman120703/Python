# Measure the performance of a func using generators and decorators
# Name = Indrajeet Mondal; Date = 7th October 2023
# SourceCode

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Time taken: {t2 - t1} s !!')
        return result

    return wrapper


@performance
def long_time():
    for i in range(10000000):
        var = i * 5


@performance
def long_time2():

    for i in list(range(10000000)):
        var = i * 5


long_time()
long_time2()
