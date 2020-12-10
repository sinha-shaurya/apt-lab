l = list(map(int, input().split()))
x = []
for i in range(len(l),2):
    if(i+1 % 2 != 0):
        x.append(l[i])
    print(i)
x.sort(reverse=True)
print(x)
count=0
for i in range(len(l)):
    if(i%2==0):
        l[i]=x[count]
        count=count+1
print(l)