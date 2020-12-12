import os
import random
import string

d={}
x=[]
for i in range(10):
    d[random.randrange(1,10)]=random.randrange(1,100)
    x.append(random.randrange(1,1000))

def dict_sort():
    x={}
    global d
    for key in sorted(d):
        x[key]=d[key]
    print(x)
    d=x
dict_sort()
print(d)
print(x)
x.sort(reverse=True)
print(x)
