a=int(input())
b=int(input())
c=int(input())
if a>b:
    if a>c:
        print(f"{a} is bigger")
    else:
        print(f"{c} is bigger")
else:
    if b>c:
        print(f"{b} is bigger")
    else:
        print(f"{c} is bigger")