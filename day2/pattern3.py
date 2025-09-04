def pattern():
    n=int(input("Enter the number"))
    return n
z=pattern()
for i in range(0,z):
    for j in range(0,z):
        if j==i or ((j+i)==z-1):
            print("$",end=" ")
        else:
            print("*",end=" ")
    print()