# check if a string starts and ends with the same character using regex
import re

s = input("Enter a string: ")

# searching
regex = r'^[a-z]$|^([a-z]).*\1$'
check = re.search(regex, s)
print(check != None)
