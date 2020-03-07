# OOP class: Task 1. Створити клас машина з атрибутами name,  make, model та методами start та stop, 
# які виводять інформацію про те що автомобіль стартував чи зупинився відповідно.
class Car:
    '''instance of the vehicle'''
    def __init__(self, owner, make, model):
        self.o = owner
        self.m = make
        self.mod = model

    def start(self):
        print("%s just started his %s %s!" % (self.o, self.m, self.mod))

    def stop(self):
        print("%s just stopped his %s %s!" % (self.o, self.m, self.mod))

car1 = Car('Alex', 'Toyota', 'Corolla')

car1.start()
car1.stop()

# OOP class: Task 2. Створити клас особа,  в якому конструктор встановлює ім’я, а метод info виводить повідомлення 
# “Hello, my name is {ім’я конкретного екземпляра класу}”, а також створити клас автомобіль,  
# в якому конструктор встановлює ім’я, а метод move виводить повідомлення 
{ім’я конкретного екземпляра класу}  moves at the speed {speed(цей параметр метод moveотримує як вхідний)} km / h
class Person:
    def __init__(self, name):
        self.n = name
    
    def info(self):
        print("Hello, my name is %s!" %self.n)

class Vehicle:
    def __init__(self, name):
        self.n = name
    
    def move(self,speed):
        self.speed = speed
        print("%s moves at the speed of %d" %( self.n, self.speed))
    
    def speed_limit_sign(self):
        self.speed_limit = 30
        print("%s moves %d but speed limit is %d!!!" %( self.n, self.speed, self.speed_limit))
        return self.speed_limit
    
    def slow_down(self):
        self.speed = self.speed_limit_sign()
        print("%s noticed speed limit sign %d and slowed down to speed %d!!!" %( self.n, self.speed_limit, self.speed))



car2 = Vehicle('Toyota')
car2.move(90)
print(car2.speed)
#car2.speed_limit_sign()
#print(car2.speed_limit)
car2.slow_down()
#print(car2.speed)
#print(car2.speed_limit)
car2.move(100)
car2.speed_limit_sign()