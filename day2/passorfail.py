def grade(a):
    return a
x=int(input("Enter the marks"))
z=grade(x)
if z>=40:
    if z>80:
        print("Distinction")
    elif z>=71 and z<=80:
        print("Grade A")
    elif z>=51 and z<71:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Fail")
    
