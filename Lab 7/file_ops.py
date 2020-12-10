# create  input file and validate emails to another file
import os
import re

# open files
filepath = "/home/shaurya/Desktop/apt-lab/Lab 7/input.txt"
f = open(filepath, encoding='utf-8')
output = open("/home/shaurya/Desktop/apt-lab/Lab 7/invalid.txt",
              mode='w', encoding='utf-8')

# validate emails


def invalidate(line):
    return (re.search('@', line) == None)


for i in f:
    if(invalidate(i)):
        output.write(i)

# flush all streams
output.flush()
f.flush()
# close all streams
output.close()
f.close()
