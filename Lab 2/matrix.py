# matrix problem
def remove_zero(x):
    return [value for value in x if value != 0]


n, n2 = map(int, input("Enter order of matrix 1\n").split())
print("Enter matrix 1")
m1 = {}
for i in range(n):
    x = list(map(int, input().split()))
    assert(len(x) == n2)
    m1[i] = remove_zero(x)
print("matrix 1", m1)
m, c = map(int, input("Enter order of matrix 2\n").split())
print("Enter matrix 2")
m2 = {}
for i in range(m):
    x = list(map(int, input().split()))
    assert(len(x) == c)
    m2[i] = remove_zero(x)

print("matrix 2", m2)


def add_lists(x, y):
    assert (len(x) == len(y))
    z = []
    for i in range(len(x)):
        z.append(x[i]+y[i])
    return z


key1 = m1.keys()
key2 = m2.keys()

ans = m1

for key, value in m1.items():
    if(key in key2):
        # add from m2
        m1[key] = add_lists(m1[key], m2[key])

for key, value in m2.items():
    if(key not in key1):
        m1[key] = value
print("result", m1)
