def prime():
    n=int(input("Enter the number"))
    return n
x=prime()
count=0
if x<=1:
    print(f"{x} is not a prime number")
else:
    i=2
    while i<x:
        if x%i==0:
            count=count+1
        else:
            count=count
    i=i+1
if count==2:
    print(f"{x} is a prime number")
else:
     print(f"{x} is a not prime number")
