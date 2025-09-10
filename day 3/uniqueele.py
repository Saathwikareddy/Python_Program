empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
visited=[]
for i in range(n):
    if empty[i] not in visited:
        visited.append(empty[i])
print(f"unique elements in the list are:{visited}")