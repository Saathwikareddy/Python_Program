def fact():
    n=int(input("Enter number"))
    return n
x=fact()
i=x
fact=1
while i>=1:
    fact=fact*i
    i=i-1
print(f"factorial of {x} is {fact}")
