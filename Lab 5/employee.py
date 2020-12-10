# store employee details into tuples

# define function to search in list

def search(l, id):
    for i in l:
        if(i[0] == id):
            return i
    return None


n = int(input("Enter number of employees\n"))
l = []
for i in range(n):
    # enter employee details
    id = input("Enter employee id:\t")
    name = input("Enter employee name:\t")
    salary = float(input("Enter employee salary:\t"))
    department = input("Enter department:\t")
    # create tuple
    t = (id, name, salary, department)
    l.append(t)
#searching
id = input("Enter search id")
res = search(l, id)
if(res == None):
    print("Not found")
else:
    print("Found ", res)
