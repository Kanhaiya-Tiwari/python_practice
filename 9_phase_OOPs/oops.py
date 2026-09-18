from abc import ABC, abstractmethod


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_parent_details(self):
        print(f"{self.name} is the parent age {self.age}")


student1 = Student("kanha", 22)
print (student1.name, student1.age)
student2 = student1

student1.student_parent_details()
student2.student_parent_details()
print (student1.age)


# Practice Programs
# Create a Student class with name and age.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def student_parent_details(self):
        print(f"{self.name} is the parent age {self.age}")
# Create multiple student objects.
student1 = Student("kanha", 22)
student2 = Student("rahul", 25)

# Create a Server class with hostname, ip, and status().
class Server:
    def __init__(self, hostname, ip):
        self.hostname = hostname
        self.ip = ip

    def status(self):
        print(f"Server {self.hostname} with IP {self.ip} is running.")
# Implement inheritance using Vehicle and Car.
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def vehicle_info(self):
        print(f"Vehicle: {self.make} {self.model}")
vehicle1 = Vehicle("Toyota", "Camry")
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def car_info(self):
        print(f"Car: {self.make} {self.model} with {self.doors} doors")
car1 = Car("Honda", "Civic", 4)
# Demonstrate method overriding with Animal and Dog.
class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
dog1 = Dog()
# Create a class with a private variable and access it through methods.
class Student:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age    # Private variable

    def get_details(self):
        return f"Name: {self.__name}, Age: {self.__age}"
student1 = Student("kanha", 22)
print(student1.get_details())

# Implement an abstract class for a payment system.


class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

# Create a utility class using a @staticmethod.
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
# Use a @classmethod to update a class variable.
class MyClass:
    count = 0

    @classmethod
    def increment_count(cls):
        cls.count += 1
# Override __str__() to display object information.
class MyClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"MyClass object with name: {self.name}"
            