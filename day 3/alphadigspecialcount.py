name=str(input("Enter the string:"))
alphacount=0
digitcount=0
specialcount=0
for i in name:
    if i.isalpha():
        alphacount+=1
    elif i.isdigit():
        digitcount+=1
    else:
        specialcount+=1
print(f"Number of alphabets in {name} are:{alphacount}")
print(f"Number of digits in {name} are:{digitcount}")
print(f"Number of special characters in {name} are:{specialcount}")
