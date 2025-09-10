empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
visited=[]
count=0
for i in range(n):
    if empty[i] in visited:
        count+=1
    visited.append(empty[i])
print(f"Total duplicate elements in the list are:{count}")

    