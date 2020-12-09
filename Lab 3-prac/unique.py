# input list and return only unique elements of the list

def unique(x):
    d = {}
    for i in x:
        if (i not in d.keys()):
            d[i] = 1
    # get values
    return [key for key, value in d.items() if value == 1]


x = list(map(int, input("Enter a list").split()))
print(unique(x))
