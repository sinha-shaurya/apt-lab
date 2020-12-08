#count number of words
s=input("Enter sentence\n")
d={}
x=s.split(" ")
count=1
sum=0
for i in x:
    key=d.keys()
    if(i in key):
        d[i]=d[i]+1
    else:
        d[i]=1
    count=count+1
for key,values in d.items():
    sum=sum+values
print(d)
print(sum)