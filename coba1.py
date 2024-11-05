class Employee:
    def __init__(self, name, age, salary):
        self.name = name;
        self.__age = age; # private  attribute
        self.salary = salary;
        
    def greeting(self):
        return f"Hello, my name is {self.name} and I am in {self.__age}";

class  Manager(Employee):
    def __init__(self,name, age, salary, department):
        super().__init__(name, age, salary);#inheritance
        self.department = department;
    
    # polimorfisme
    def  greeting(self):
        return f"Hello, my name is {self.name} and I am in {self.department}";


joni = Manager("Herman", 31, 10000000, "Tech");
jono = Employee("Jono", 27, 15000000);
print(jono.greeting());
print(joni.greeting());