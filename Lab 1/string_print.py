#string problem
n=int(input("Enter number of strings"))
l=[]
for i in range(n):
    x=input("")
    if(len(x)>=2):
        if(x[0]==x[len(x)-1]):
            l.append(x)
for i in l:
    if(len(i)%2==1):
        print(i)