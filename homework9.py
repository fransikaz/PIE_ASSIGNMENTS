'''
HOMEWORK #9: Classes by Frank Sikazwe
Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
Next an inheritance classes from Vehicle called "Cars".
The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.
It should have another method called "Stop" that sets the value of isDriving to false.
Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter.
And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.
Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
Create 3 different cars, using your Cars class, and drive them all a different number of times.
Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance

'''


class Vehicle:  # Base class
    def __init__(self, make, model, year, weight, TripsSinceMaintenance=0, NeedsMaintenance=False):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.NeedsMaintenance = NeedsMaintenance
        self.TripsSinceMaintenance = TripsSinceMaintenance

    def DefineMake(self, make):
        self.make = make

    def Definemodel(self, model):
        self.model = model

    def DefineYear(self, year):
        self.year = year

    def DefineWeight(self, weight):
        self.weight = weight

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return "{:<10}{:<20}{:<10}{:<10}{:<30}{:<40}".format(self.make, self.model, self.year, str(self.weight), str(self.TripsSinceMaintenance), str(self.NeedsMaintenance))


class Cars(Vehicle):  # Inheritance class from Vehicle
    def __init__(self, make, model, year, weight, TripsSinceMaintenance, NeedsMaintenance, isDriving):
        Vehicle.__init__(self, make, model, year, weight, TripsSinceMaintenance,
                         NeedsMaintenance)
        self.isDriving = isDriving

    def Drive(self, isDriving):  # Method for setting isDriving to True
        self.isDriving = True

    def Stop(self, isDriving):  # Method for setting isdriving to False
        self.isDriving = False
        self.TripsSinceMaintenance += 20
        if self.TripsSinceMaintenance > 100:
            self.NeedsMaintenance = True


class Plane(Vehicle):  # Class Plane inheriting objects from Vehicle
    def __init__(self, make, model, year, weight, TripsSinceMaintenance, NeedsMaintenance, isFlying):
        Vehicle.__init__(self, make, model, year, weight,
                         TripsSinceMaintenance, NeedsMaintenance)
        self.Flying = isFlying

    def Flying(self):
        if self.NeedsMaintenance == False:
            self.isFlying = True
        else:
            self.isFlying = False
            print("Plane can't fly until repaired")

    def Landing(self, isFlying):
        self.isFlying = False
        self.TripsSinceMaintenance += 500
        if self.TripsSinceMaintenance > 1000:
            self.NeedsMaintenance = True


Car1 = Cars("Toyota", "Supra", "2018", 1500, 60, False, False)
Car2 = Cars("BWM", "3 Series", "2019", 1700, 0, False, False)
Car3 = Cars("Tesla", "Model Y", "2018", 2000, 90, False, False)
Plane1 = Plane("Boeing", "747", "1970", 10000, 940, False, True)

#  printing headers
print("{:<10}{:<20}{:<10}{:<10}{:<30}{:<40}".format("Make", "Model", "Year",
                                                    "Weight", "TripsSinceMaintenance", "NeedsMaintenance"))
print(Car1)
print(Car2)
print(Car3)
print()

Car1.Drive(True)  # Driving Car1
Car1.Stop(True)  # Stopping Car1

#  printing table headers
print("{:<10}{:<20}{:<10}{:<10}{:<30}{:<40}".format("Make", "Model", "Year",
                                                    "Weight", "TripsSinceMaintenance", "NeedsMaintenance"))
# Printing Car attributes
print(Car1)
print(Car2)
print(Car3)
print()

Car1.Drive(True)  # Driving Car1
Car1.Stop(True)  # Stopping Car1
Car2.Drive(True)  # Driving Car2
Car2.Stop(True)  # Stopping Car2

#  printing table headers
print("{:<10}{:<20}{:<10}{:<10}{:<30}{:<40}".format("Make", "Model", "Year",
                                                    "Weight", "TripsSinceMaintenance", "NeedsMaintenance"))
# Printing Car attributes
print(Car1)
print(Car2)
print(Car3)
print()

Car1.Drive(True)  # Driving Car1
Car1.Stop(True)  # Stopping Car1
Car2.Drive(True)  # Driving Car2
Car2.Stop(True)  # Stopping Car2
Car3.Drive(True)  # Driving Car3
Car3.Stop(True)  # Driving Car1
Plane1.Landing(True)  # Landing Plane 1

# printing table headers
print("{:<10}{:<20}{:<10}{:<10}{:<30}{:<40}".format("Make", "Model", "Year",
                                                    "Weight", "TripsSinceMaintenance", "NeedsMaintenance"))
# Printing Car attributes
print(Car1)
print(Car2)
print(Car3)
print(Plane1)
print()

Plane1.Flying(True)

# Car1 and Car3 taken for maintenance
Car1.Repair()
Car3.Repair()
Plane1.Repair()

# printing table headers
print("{:<10}{:<20}{:<10}{:<10}{:<30}{:<40}".format("Make", "Model", "Year",
                                                    "Weight", "TripsSinceMaintenance", "NeedsMaintenance"))
# Printing Car attributes
print(Car1)
print(Car2)
print(Car3)
print(Plane1)
print()
