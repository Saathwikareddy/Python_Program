empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
first=second=-999999999
for i in range(n):
    if empty[i]>first:
        second=first
        first=empty[i]
    elif empty[i]>second and empty[i]!=first:
        second=empty[i]
print(f"Second largest element is:{second}")

