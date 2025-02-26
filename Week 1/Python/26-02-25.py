# # f(x, y) = x + 2 + xy


# from functools import reduce


# def eqn1(x, y=1, z=0):
#     c = x + 2 + x*y + z
#     return c

# a = 10
# b = 90
# c = 10
# print(eqn1(a, b, c))


# def greet(name):
#     print("Hello, " + name)

# greet("femi")

# # Create a function any number of arguments and sums them up
# # result = sum(1, 2, 3, 4, 5) => 15

# def example1(**kwargs):
#     return kwargs
  
# print(example1(a=10, b=20, name="Femi"))

# # Lambda
# x = lambda a: a + 1
# print(x(100))

# # def x(a):
# #   return a + 1

# def sum(*args):
#     return reduce(lambda x, y: x + y, args)

# print(sum(1, 2, 3, 4, 5))





# Scope
from re import S


def myfunc():
    x = 300
    print(x)
    def inner1():
        z = 100
        print(x)
        print(z)
        def inner_deeper():
            y = 10
            print(x)
            print(z)
            print(y)
        print(z)
        inner_deeper()
    inner1()

# myfunc()

# Modules
# from mathematics import calculator

# print(calculator.add(10, 20))
# print(calculator.subtract(10, 20))
# print(calculator.multiply(10, 20))
# print(calculator.divide(10, 20))

# from mathematics.calculator import add
# print(add(10, 20))

# from mathematics.calculator import *
# print(subtract(10, 20))

# from platform import system, version
# print(system())
# print(version())


def err_handling():
    from mathematics.calculator import divide
    # Error handling
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        print(divide(a, b))
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except ValueError:
        print("You must enter a number")
    except Exception as e:
        print("An error occurred: ", e)

    print("This is the end of the program")

# err_handling()

# Classes
class SquarePan:
    x = 5
    
    def __init__(self):
        print("I am a constructor")

bread = SquarePan()
print(bread.x)

bread2 = SquarePan()
print(bread2.x)

class Person:
    name: str
    age: int
    gender: str
    
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def talk(self, message):
        print(message)
    
    def walk(self):
        print("I am walking")
    
    def greet(self):
        self.talk("Hello, my name is " + self.name)

femi = Person("Femi", 30, "Male")
eednut = Person("Eednut", 40, "Female")

print(femi.name)
print(femi.talk("How are you"))
print(femi.walk())
print(femi.greet())

class Engine:
    fuel_pump: str
    name: str

    def __init__(self, fuel_pump, name):
        self.fuel_pump = fuel_pump
        self.name = name

    def start(self):
        print(f"{self.name} Engine started")

    def stop(self):
        print(f"{self.name} Engine stopped")

class SteeringWheel:
    type: str
    size: int

class Car:
    model: str
    engine: Engine
    steering_wheel: SteeringWheel
    
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine

    def start(self):
        self.engine.start()
        print("Car started")
    
    def stop(self):
        self.engine.stop()
        print("Car stopped")


engine1 = Engine("Fuel Pump", "V8")
engine2 = Engine("Fuel Pump", "V6")

car1 = Car("Toyota", engine1)
car2 = Car("Honda", engine2)

car1.start()
car1.stop()
car2.start()
car2.stop()