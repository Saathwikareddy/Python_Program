def pattern():
    n=int(input("Enter the number"))
    return n
z=pattern()
for i in range(0,z):
    for j in range(0,z):
        print("*",end=" ")
    print()