"""
Program: Rider.py
Author:  Luke Xiong
Date: 7/12/2020

This program is an abstractmethod with subclasses
"""
from abc import ABC, abstractmethod

class Rider(ABC):
    @abstractmethod
    def descript(self):
        pass

class InvalidSideError(Exception):
    pass

class Bicycle(Rider):
    def __init__(self):#(self, bike):
        #name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        #if not (name_characters.issuperset(bike)):
            #raise InvalidSideError
        self.bike = ('Human powered, not enclosed' + '\n' + '1 or 2 if tandem or a daredevil')

    def descript(self):
        return self.bike

    def __str__(self):
        return str(self.descript())


class Motorcycle(Rider):
    def __init__(self):#(self, motorcycle):
        #name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        #if not (name_characters.issuperset(motorcycle)):
            #raise InvalidSideError
        self.motorcycle = ('Engine powered, not enclosed' +'\n'+'1 or 2')

    def descript(self):
        return self.motorcycle

    def __str__(self):
        return str(self.descript())


class Car(Rider):
    def __init__(self):#(self, car):
        #name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        #if not (name_characters.issuperset(car)):
            #raise InvalidSideError
        self.car = ('Engine powered, enclosed'+'\n'+'1 plus comfortably')

    def descript(self):
        return self.car

    def __str__(self):
        return str(self.descript())

# Driver code
b = Bicycle()
print(str(b))
m = Motorcycle()
print(str(m))
c = Car()
print(str(c))


