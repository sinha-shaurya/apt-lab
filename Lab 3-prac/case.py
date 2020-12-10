# calculate number of lowercase and uppercase letters
import string

s = input("Enter a string")
# check for uppercase and lowercase letters
lc = 0
uc = 0
for i in s:
    if(i in string.ascii_lowercase):
        lc = lc+1
    elif (i in string.ascii_uppercase):
        uc = uc+1
print("Number of uppercase letters=", uc, "\nNumber of lowercase letters=", lc)
