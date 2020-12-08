# random key dictionary
import random
import string
n = int(input("Enter number of values for dictionary"))
d = {}
for i in range(n):
    x = input("")
    d[random.randrange(0, 100)] = x
# find average
sum = 0
x = ""
nums=0
for key, value in d.items():
    if(value.isdecimal()):
        sum=sum+int(value)
        nums=nums+1
    else:
        if(type(value) == str):
            x = x+value
print("Average of the numeric values present=", (sum/nums))
print(x)

val = input("Enter value\n")
assert (type(val) == str)

for key, value in d.items():
    if(value == val):
        print("value found with key as",key)
#to find special character strings
regex = string.ascii_letters+string.digits
for key, value in d.items():
    flag = True
    # check invidually
    for i in range(len(value)):
        if(value[i] in regex):
            flag = False
            break
    if(flag == True):
        print(value)
