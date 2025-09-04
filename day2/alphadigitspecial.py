def alphadigit():
    a=input("Enter a character")
    return a
z=alphadigit()
if z.isalpha():
    if z.isupper():
        print(f"{z} is  capital alphabet")
    else:
        print(f"{z} is lower alphabet")
elif z.isdigit():
    print(f"{z} is a digit")
else:
    print(f"{z} is special character")