sturec=()
n=int(input("Enter the number of tuples:"))
for i  in range(n):
    name=input("Enter the name:")
    rollno=int(input("Enter the roll number:"))
    marks=int(input("Enter the marks:"))
    sturec=sturec+((name,rollno,marks),)
print(f"Student records are:{sturec}")
highestmarks=sturec[0][2]
for i in range(n):
    if sturec[i][2]>highestmarks:
        highestmarks=sturec[i][2]
print(f"Name of the student with highest marks is:{sturec[i][0]}")
for i in range(n):
    if sturec[i][2]>75:
        print(f"Students with marks greater than 75 are:{sturec[i][0]}")

