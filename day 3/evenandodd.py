empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
evencount=0
oddcount=0
for i in range(n):
    if empty[i]%2==0:
        evencount+=1
    else:
        oddcount+=1
print(f"Even count is:{evencount}")
print(f"odd count is:{oddcount}")
