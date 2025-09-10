name=str(input("Enter the string:"))
char=str(input("Enter the character to find"))
positions=[]
for i in range(len(name)):
    if name[i]==char:
        positions.append(i)
print(f"Character found:{positions}")