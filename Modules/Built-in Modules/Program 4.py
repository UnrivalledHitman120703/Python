# datetime and array module
# Name = Indrajeet Mondal; Date = 17th October 2023
# SourceCode

import datetime
from array import array

# Getting the current system time
print(datetime.time())
# Creating a custom time object by passing the required time as argument
print(datetime.time(5, 45,2))

# Getting the current date
print(datetime.date.today())

# Arrays are static lists, their length is specified while creating it only
arr = array('i', [1,2,3])
print(arr[0])
