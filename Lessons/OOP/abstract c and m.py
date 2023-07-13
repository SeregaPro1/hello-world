# prevent a user form creating an object of that  class
# + comples a user to override abstrack methods in a child class

# abstract class = a class which contains one or more abstract mthods.
# abstract method = a method  that has dclatartion but does not have an implementation

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):

    def go(self):
        print('You drive the car')

    def stop(self):
        print('This car if stopped')

class Motorcycle(Vehicle):

    def go(self):
        print('You ride the motorcycle')

    def stop(self):
        print('This motorcycle if stopped')

car = Car()
# vehicle = Vehicle()
motorcycle = Motorcycle()

# vehicle.go()
car.go()
motorcycle.go()