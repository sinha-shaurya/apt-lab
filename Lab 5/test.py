id=1

class emp():
    def __init__(self):
        global id
        self.eid=id
        id=id+1
    
    def display(self):
        print(self.eid)
    def __del__(self):
        print("deleted")

e=[]
for i in range(10):
    x=emp()
    e.append(x)

for i in e:
    i.display()

for i in e:
    del i