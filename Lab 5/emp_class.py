class employee():
    @staticmethod
    def search(list, id):
        for i in list:
            if i.id == id:
                print(i.name,i.id)
                return i
        return None
        pass

    def __init__(self, name, id):
        self.id = id
        self.name = name


a = employee("shau", 12)
b = employee("bob", 14)
c = employee("alice", 13)
list = []
list.append(a)
list.append(b)
list.append(c)
print(employee.search(list,14))
