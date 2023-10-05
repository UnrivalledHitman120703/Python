# Method Resolution Order
# Name = Indrajeet Mondal; Date = 5th October 2023
# SourceCode

class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


# Visualisation of the above multiple inheritance
#                      A
#                   /     \
#                  /       \
#                 B         C
#                  \       /
#                   \     /
#                      D

print(D.mro())
