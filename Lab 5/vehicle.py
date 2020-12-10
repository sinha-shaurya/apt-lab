# define a class vehicle with attributes and derive a class passenger from it

class Vehicle:

    # constructor
    def __init__(self, name, vin, mname):
        self.name = name
        self.vin = vin
        self.mname = mname


class Passenger(Vehicle):

    # constructor
    def __init__(self):
        # input details for the vehicle
        name = input("Enter name: ")
        vin = input("Enter vehicle identification number: ")
        mname = input("Enter manufacturer name: ")
        np = int(input("Enter number of passengers: "))
        super().__init__(name, vin, mname)
        self.np = np

    # display details
    def display_details(self):
        print("Name: ", self.name, "\nVIN: ", self.vin,
              "\nManufacturer: ", self.mname, "\nNumber of Passengers: ", self.np)


a = Passenger()
a.display_details()
