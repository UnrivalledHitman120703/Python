# Creating a sample program to run tests on
# Name = Indrajeet Mondal; Date = 11th October 2023
# SourceCode

# Creating a function
def do_stuff(num):
    if num is None:
        return 'Please enter an integer value'
    try:
        return int(num) + 5
    except ValueError:
        return ValueError("Input must be an integer.")

