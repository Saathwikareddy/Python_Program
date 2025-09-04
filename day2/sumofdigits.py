def sum():
    n=int(input("Enter a number"))
    return n
z=sum()
sumdigits=0
for i in str(z):
    sumdigits = sumdigits + int(i)
print("sum is:",sumdigits)
