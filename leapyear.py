a=int(input("Enter year"))
if (a%100==0 and a%4==0) or a%400==0:
    print(f"{a} is a leap year")
else:
    print(f"{a} is not a leap year")

    