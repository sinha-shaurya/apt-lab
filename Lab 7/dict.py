# count occurrences of each word in a file
import os
d = {}

# function to put into dictionary


def put(line):
    s = line.split()
    for i in s:
        if i in d.keys():
            d[i] = d[i]+1
        else:
            d[i] = 1


filepath = "file.txt"
#open file, default mode is read, encoding is platform dependent but is mostly UTF-8
f = open(filepath)

for line in f:
    put(line)
print("Word\tFrequency")
for key, value in d.items():
    print(key,"\t",value)

