def week():
    a=int(input("Enter the number between 1 and 7:"))
    return a
z=week()
if z==1:
    print("Sunday")
elif z==2:
    print("Monday")
elif z==3:
    print("Tuesday")
elif z==4:
    print("wednesday")
elif z==5:
    print("Thursday")
elif z==6:
    print("Friday")
elif z==7:
    print("Saturday")
else:
    print("Invalid number")