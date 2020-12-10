# count total numbers of characters, words and lines in a file
import os

filepath = "file.txt"
file = open(filepath, 'r', encoding='utf-8')

chars = 0
words = 0
lines = 0
# read file line by line
for line in file:
    lines = lines+1
    chars = chars+len(line)
    s = line.split()
    words = words+len(s)
    print(line)

print("Number of lines=",lines,"\nNumber of characters=",chars,"\nNumber of words=",words)

