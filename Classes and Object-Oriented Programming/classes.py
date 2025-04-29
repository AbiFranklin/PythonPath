# Typically used for debugging purposes only
# class Employee:
#     def __init__(self):
#         self.__dict__["name"] = "Ji-Soo"
#         self.__dict__["age"] = 30
#         self.__dict__["position"] = "Software Engineer"
#         self.__dict__["salary"] = 80000


# Class definition for Employee
# class Employee:
#     def __init__(self, name, age, position, salary):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary

#     # Instance methods/functions for the Employee class
#     def increase_salary(self, percent):
#         self.salary += self.salary * (percent / 100)

#     # def employee_info(self):
#     #     return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary:.2f}"

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary:.2f}"

#     def __repr__(self):
#         return f"Employee({self.name!r}, {self.age!r}, {self.position!r}, {self.salary!r})"


# # Creating instances of the Employee class
# employee1 = Employee("Ji-Soo", 30, "Software Engineer", 80000)
# employee2 = Employee("Lauren", 28, "Data Scientist", 75000)

# print(employee1.name)
# # print(employee2.employee_info())
# employee1.increase_salary(10)
# # print(employee1.employee_info())
# print(repr(employee1))
# print(eval(repr(employee1)))

# __new__ allocates memory for the new object and sends it to __init__
# __init__ receives a new object from the __new__ method as a "self" argument and initializes it

# class Employee:
#     def __init__(self, name, age, position, salary):
#         # Initialize the object with attributes
#         self.name = name
#         self.age = age
#         self.position = position
#         self.salary = salary
#         self._annual_salary = None

#     def increase_salary(self, percent):
#         # Increase the salary by a percentage
#         self.salary += self.salary * (percent / 100)

#     def __str__(self):
#         # String representation of the object
#         return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary:.2f}"

#     def __repr__(self):
#         # Official string representation of the object
#         return f"Employee({self.name!r}, {self.age!r}, {self.position!r}, {self.salary!r})"

#     @property
#     def salary(self):
#         # Getter method for salary
#         return self._salary

#     @salary.setter
#     def salary(self, value):
#         # Setter method for salary with validation
#         if value < 1000:
#             raise ValueError("Salary cannot be less than $1000.")
#         self._annual_salary = None  # Reset annual salary when salary is updated
#         self._salary = value

#     @property
#     def annual_salary(self):
#         # Getter method for annual salary
#         if self._annual_salary is None:
#             self._annual_salary = self.salary * 12
#         return self._annual_salary


# e = Employee("Ji-Soo", 30, "Software Engineer", 8000)
# e.salary = 8500
# print(e.salary)

# Pillars of OOP:
# 1. Encapsulation: Bundling data and methods that operate on that data within a single unit (class). Hiding the internal state of the object and requiring all interaction to be performed through an object's methods.
# 2. Abstraction: Hiding complex implementation details and exposing only the necessary parts of an object.
# 3. Inheritance: Mechanism to create a new class that inherits attributes and methods from an existing class, allowing for code reuse.
# 4. Polymorphism: Ability to present the same interface for different underlying data types. In Python, this is often achieved through method overriding and duck typing.

# Name mangling: In Python, name mangling is a mechanism to prevent name clashes in subclasses. It is done by prefixing the attribute name with two underscores (`__`). This makes the attribute name harder to access from outside the class, as it gets transformed to `_ClassName__attributeName`.
# The purpose of @property is to provide a way to define methods in a class that can be accessed like attributes. It allows you to create getter and setter methods for an attribute without needing to call them as methods, thus providing a cleaner interface for the class users.


# # Superclass
# class Employee:
#     __slots__ = (
#         "name",
#         "age",
#         "salary",
#     )  # Limiting attributes to 'name', 'age', and 'salary'

#     def __init__(self, name, age, salary):
#         # Initialize the object with attributes
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def increase_salary(self, percent):  # Increase the salary by a percentage
#         self.salary += self.salary * (percent / 100)

# class SlotsInspectorMixin:
#     __slots__ = ()  # This mixin can be used to check for slots in subclasses

#     def has_slots(self):
#         return hasattr(self, '__slots__')

# # Subclass
# class Tester(Employee):
#     def run_tests(self):
#         print(f"{self.name} is running tests.")
#         print("Tests are complete.")


# # Subclass
# class Developer(SlotsInspectorMixin, Employee):
#     __slots__ = "framework"  # Limiting attributes to 'framework' in addition to those in Employee

#     def __init__(self, name, age, salary, framework):
#         super().__init__(name, age, salary)
#         self.framework = framework

#     # Method overriding the increase_salary method
#     def increase_salary(self, percent, bonus=0):
#         super().increase_salary(percent)
#         self.salary += bonus


# t = Tester("Ji-Soo", 30, 80000)
# t.run_tests()
# d = Developer("Lauren", 28, 75000, "JS")
# d.increase_salary(10, 5000)
# print(d.salary)
# # print(d.__dict__) #Throws an error because __slots__ is used in subclass and both superclasses, and __dict__ is not available
# print(d.__slots__)  # This will show the limited attributes defined in __slots__
# print(d.has_slots())  # Check if the instance has __slots__

# isinstance can be used to check if an object is an instance of a class or a subclass of that class.
# issubclass can be used to check if a class is a subclass of another class.
# super() is used to call a method from a parent class in a subclass, allowing for method overriding and extension of functionality.
#   Method Resolution Order (MRO) is the order in which Python looks for a method in a hierarchy of classes. It determines the order in
#   which classes are searched when calling a method on an instance of a class. You can view the MRO of a class using the `__mro__` attribute or the `mro()` method.
# Slots are a way to limit the attributes that can be added to an instance of a class, which can lead to performance improvements in memory usage.
#   Cannot add new attributes to instances of a class that uses `__slots__` beyond those defined in the `__slots__` tuple.

# from datetime import date


# class Employee:
#     minimum_wage = 1000  # Class variable for minimum salary

#     @classmethod
#     def change_minimum_wage(cls, new_wage):
#         if new_wage > 3000:
#             raise ValueError("Minimum wage cannot exceed $3000.")
#         cls.minimum_wage = new_wage

#     @classmethod
#     def new_employee(cls, name, dob):
#         age = date.today().year - dob.year - ((date.today().month, date.today().day) < (dob.month, dob.day))
#         return cls(name, age, cls.minimum_wage)

#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary

#     def increase_salary(self, percent):
#         self.salary += self.salary * (percent / 100)

#     @property
#     def salary(self):
#         return self._salary

#     @salary.setter
#     def salary(self, value):
#         if value < self.minimum_wage:
#             raise ValueError("Salary cannot be less than $1000.")
#         self._salary = value


# e = Employee("Ji-Soo", 30, 8000)
# Employee.__dict__["increase_salary"](e, 10)
# print(e.salary)
# print(e.minimum_wage)  # Accessing class variable directly from the instance
# new_employee = Employee.new_employee("Lauren", date(1995, 5, 15))
# print(new_employee.name, new_employee.age, new_employee.salary)

from dataclasses import dataclass

@dataclass(slots=True)
class Project:
    name: str
    payment: float
    client: str

    def notify_client(self):
        return f"Notification sent to {self.client} for project {self.name}."

class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project

p = Project("AI Development", 150000, "TechCorp")
e = Employee("Ji-Soo", 30, 80000, p)
print(e.project)  # This will print the project details using the __str__ method of Project class

#  A dataclass is a decorator that automatically generates special methods for classes, such as __init__, __repr__, and __eq__, based on class attributes. It simplifies class creation by reducing boilerplate code.