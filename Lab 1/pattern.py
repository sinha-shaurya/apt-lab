#generate pattern 
count=1
for i in range(6):
    for j in range(i):
        print(count,end=" ")
        count=count+1
    print("\n")