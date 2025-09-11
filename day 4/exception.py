x=int(input("Enter x:"))
y=int(input("Enter y:"))
try:
    z=x/y
    print(f"Result is:{z}")
except ZeroDivisionError:
    print("Denominator cannot be zero")