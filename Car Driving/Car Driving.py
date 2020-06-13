import random
class Car:

    import random
    

    def __init__(self, name, maf, color, year, cc):
        self.name = name
        self.manufacturer = maf
        self.color = color
        self.year = year
        self.cc = cc

    def start(self):
        print("Car Details")
        print(f"Car: {self.name} \n Manufacturer: {self.manufacturer}")
        print(f"Color: {self.color} \n Year: {self.year}")
        print(f"Power: {self.cc}cc")
        print("Starting the engine")

    def brake(self):

        Brake = input("Do you want to Brake?: ")
        if Brake in ["Yes", "yes", "brake", "Brake"]:
            print("Car is stoping")
            

        else:
            print("Car is still runing")

    def drive(self):
        
        print("Please keep driving")

    def turn(self):
        
        x = input("Which side do you want to go?: ")
        if x in ["Left", "left"]:
            print(f"{self.name} is turning Left")
        if x in ["Right", "right"]:
            print(f"{self.name} is turning Right")
    def cgear(self):

        
        Cgear = random.randint(1, 5)
        print("Current gear:", Cgear)
        q = input("Please select gear: ")
        q = int(q)
        if q > Cgear:
            print(f"Selected Gear: {q}, Speed is Increasing")
        elif q < Cgear:
            print(f"Selected Gear: {q}, Speed is decreasing")

name = input("Please Enter Your Car's Name: ")
maf = input("Please Enter Your Car Manufacturer's Name: ")
color = input("Please enter your Car's color: ")
year = input("Please Enter the Year: ")
cc = input("Please Enter Your Car's Power: ")
my_car = Car(name, maf, color, year, cc)

my_car.start()
my_car.brake()
my_car.drive()
my_car.turn()
my_car.cgear()
