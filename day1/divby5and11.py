def div(a):
    return a%11==0 and a%5==0
a=int(input("Enter a"))
if div(a):
    print(f"{a} is divisible by 5 and 11")
else:
    print(f"{a} is not divisible")