# Learning more about decorators, passing argument to func inside the decorator func
# Name = Indrajeet Mondal; Date = 7th October 2023
# SourceCode

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('******')
        func(*args, **kwargs)
        print('******')

    return wrap_func


@my_decorator
def hello(greeting, emoji=":)"):
    print(greeting, emoji)


hello("Hello")
