name=str(input("Enter the string:"))
count=0
for i in name:
    count+=1
print(f"Length of the string is :{count}")
name2=str(input("Enter another string:"))
if name==name2:
    print("Both the strings are equal")
else:
    print("Both the strings are not equal")
name3=name+name2
print(f"Concatenated string is:{name3}")