# multiply elements of a list
def list_muliply(x):
    p = 1
    for i in x:
        p = p*i
    return p


list = list(map(int, input("Enter a space separated list\n").split()))
print("Product of list elements=", list_muliply(list))
