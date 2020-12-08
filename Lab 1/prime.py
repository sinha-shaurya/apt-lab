#generate prime numbers between n and m 
def is_prime(n):
    count=0
    for i in range(1,n+1):
        if(n%i==0):
            count=count+1
    if(count==2):
        return True
    else:
        return False
n=int(input("Enter lower limit: "))
m=int(input("Enter uppper limit: "))
assert (m>n)
for i in range(n,m):
    if(is_prime(i)):
        print(i)