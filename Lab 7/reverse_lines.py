#print lines of file in reverse order
import os

filepath="file.txt"
#open file
f=open(filepath,encoding='utf-8')

lines=[]
for line in f:
    lines.append(line)
lines.reverse()

for i in lines:
    print(i)