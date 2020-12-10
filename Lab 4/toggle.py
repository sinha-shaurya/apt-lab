# capitalise each word of a sentence using built in modules
import string

s = input("Enter a sentence:\n")
x=s.split()
res=""
for i in x:
    res=res+i[0].upper()+i[1:]+" "
print(res)