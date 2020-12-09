# detect number of local variables in a function

def fun():
    a = 1
    b = "Shaurya"
    c = 100.0
    d = 'd'


val = fun.__code__.co_nlocals

# print number of local variables
print("Number of local variables in fun() is ", val)
