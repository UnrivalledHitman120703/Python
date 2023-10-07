# Decorator
# Name = Indrajeet Mondal; Date = 7th October 2023
# SourceCode

# HOC: A func that takes a func as an argument or returns a func

def my_decorator(func):
    print('******')

    def wrap_func():
        func()
        print('******')

    return wrap_func


# Define the hello function
def hello():
    print('Hello')


# Apply the decorator to the hello function
hello = my_decorator(hello)

# Call the decorated hello function
hello()
