def Armstrong():
    n = int(input("Enter the number: "))
    for i in range(1,n+1):
        temp=i
        sum=0
        while temp > 0:
            digit = temp % 10
            sum=sum+digit**3
            temp //= 10
        if sum==i:
            print(i)
           

Armstrong()