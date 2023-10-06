# Dictionary comprehensions
# Name = Indrajeet Mondal; Date = 6th October 2023
# SourceCode

simple_dict = {
    'a': 1,
    'b': 2
}
# Example1
my_dict1 = {key: value ** 2 for key, value in
            simple_dict.items() if value % 2 == 0}
print(my_dict1)

# Example2
my_dict2 = {num: num * 2 for num in [1, 2, 3]}
print(my_dict2)
