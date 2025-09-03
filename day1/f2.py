def kilo(a):
    b=a*0.621
    print(f"{a} in miles is:{b}")
x=int(input("Enter kilometres"))
kilo(x)


def days(a):
    years=a/365
    months=a/31
    print(f"{a} in years is:{years} and in months is:{months}")
x=int(input("Enter number of days"))
days(x)