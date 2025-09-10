empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
print("Negative elements are:")
for i in range(n):
    if empty[i]<0:
        print(empty[i])
