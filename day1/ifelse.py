def even(a):
    c=a%2
    return c
a=int(input("Enter a"))
z=even(a)
if z%2==0:
    print(f"{z} is even number")
else:
    print(f"{z} is odd number")