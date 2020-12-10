#list out all enviroment variables using Python
import os

for key,value in os.environ.items():
    print(key,":",value)
