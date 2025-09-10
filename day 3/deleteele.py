empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
del empty[2]
print(f"List after deleting:{empty}")
for i in range(n):
    if i==2:
        empty.remove(empty[i])
print(f"List after removing:{empty}")