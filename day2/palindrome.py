def palindrome():
    n = int(input("Enter the number: "))
    for i in range(1, n + 1):
        temp = i
        rev = 0
        while temp > 0:
            digit = temp % 10
            rev = rev * 10 + digit
            temp //= 10
        if i == rev:  
            print(i)

palindrome()

