# Collections Module
# Name = Indrajeet Mondal; Date = 17th October 2023
# SourceCode

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
# Counter helps to convert an item like list to a hash map/ dictionary helps in optimisation problems
print(Counter('li:- ', li))
print(Counter('sentence', sentence))

# Using defaultdict
dictionary = defaultdict(lambda:5,{'a':1, 'b':2})
print(dictionary['a'])
print(dictionary['b'])
print(dictionary['c'])

# Using OrderedDict
d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2 = {'c': 100}
d2['b'] = 2
d2['a'] = 1

print(d2 == d)

# Python has made Dictionaries ordered by default!!
# So unless we need to maintain older version of Python (older than 3.7), you no longer need to use ordered dict, you can just use regular dictionaries!
