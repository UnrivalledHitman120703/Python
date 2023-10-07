# Printing fibonacci numbers using generators
# Name = Indrajeet Mondal; Date = 7th October 2023
# SourceCode

def fib(number):
    a = 0
    b = 1
    for i in range(number):
        yield a
        temp = a
        a = b
        b += temp


for x in fib(100):
    print(x)
