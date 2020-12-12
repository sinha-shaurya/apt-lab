# create class car with given attributes

class Owner():
    def __init__(self, name, address, profession, license):
        self.name = name
        self.address = address
        self.profession = profession
        self.license = license

    def displayOwner(self):
        if(self == None):
            print("None")
        else:
            print(self.name, " ", self.address, " ",
                  self.profession, " ", self.license)


class Car():
    own = []
    car = []
    owner=Owner("s","33","ent",100)
    def __init__(self, eno, rno, rdate, colour, own:Owner, model):
        self.eno = eno
        self.rno = rno
        self.rdate = rdate
        self.colour = colour
        self.owner = own
        self.model = model

    def displayCar(self):
        print(self.eno, self.rno, self.rdate, self.colour)
        print(type(self.owner))

    #@staticmethodcl
    def init_array(self):
        #create objects of type car
        for i in range(5):
            c=Car(1000,20,"Today","Red",None,"GTX")
            self.car.append(c)
        for i in self.car:
            i.displayCar()
        #pass
o=Owner("shaurya","333","student",100)
a=Car(100,20,"Today","Red",o,"GTX")
a.init_array()