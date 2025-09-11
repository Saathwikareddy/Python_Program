class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print(f"Name of the employee is:{self.name}")
        print(f"Salary is:{self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print(f"Department is:{self.department}")
Employee1=Employee("Seeta",80000)
Employee1.display()
print("---------------------------------------")
Manager1=Manager("Ram",75000,"HR")
Manager1.display()
