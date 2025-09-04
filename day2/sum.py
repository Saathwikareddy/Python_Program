def sum():
    n=int(input("Enter the natural number"))
    return n
x=sum()
i=1
sum=0
while i<=x:
    sum=sum+i
    i=i+1
print(f"Sum up to {x} is:{sum}")