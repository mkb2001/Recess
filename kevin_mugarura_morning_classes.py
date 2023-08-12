class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Hello my name is", self.name)
        print("I am", self.age, "years old")
        
class Rectangle:
    def __init__(self, width, length) :
        self.width = width
        self.length = length
    def calculatePerimeter(self):
        return (self.width *2) + (self.length*2)
    
rect1 = Rectangle(1,2) 
print(rect1.calculatePerimeter())





class Employee:
    def __init__(self, salary):
        self.salary = salary
    
    def calculateBonuses(self):
        print("The employee has a bonus of ", self.salary *0.15)
        
employee = Employee(15000)
employee2 = Employee(230000)

employee.calculateBonuses()
employee.calculateBonuses()


#Assignment
class EmployeeInfo():
    def __init__(self, name, salary,  increament):
        self._name=name
        self._salary=salary
        self._increament=increament
    def print_employee_info(self):
        #Due to encapsulation, I cannot access the name and salary attribute directly
        print(f"{self._name}'s salary is {self._salary}. With an increament of {self._increament}, it is now {self._salary+self._increament}")
employee_info = EmployeeInfo("Davidson", 12000,300)   
employee_info.print_employee_info()    
        