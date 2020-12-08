#merge 2 lists

#setup list 1
n=int(input('Enter number of elements in list 1\n'))
list1=[]
for i in range(n):
    x=int(input(""))
    list1.append(x)

#setup list 2
m=int(input("Enter number of elements in list 2\n"))
list2=[]
for i in range(m):
    x=int(input())
    list2.append(x)

#merge
l=[]
for i in list1:
    if(i&1):
        l.append(i)
for i in list2:
    if(not(i&1)):
        l.append(i)
print(l)