class student():
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def display(self):
        print(f"Name of the student is:{self.name}")
        print(f"Roll number of the student is:{self.rollno}")
        print(f"Marks of the student is:{self.marks}")
student1=student("Seeta",1,99)
student1.display()
print("---------------------------------------")
student2=student("Ram",2,98)
student2.display()