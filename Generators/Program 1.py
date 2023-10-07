# Creating a generator
# Name = Indrajeet Mondal; Date = 7th October 2023
# SourceCode

def generator_function(num):
    for i in range(num):
        yield i


g = generator_function(100)
next(g)
next(g)
print(next(g))

# for item in generator_function(100):
#     print(item)
