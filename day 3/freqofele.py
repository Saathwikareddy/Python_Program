empty=[]
n=int(input("Enter the length of the list"))
for i in range(n):
    empty.append(int(input("Enter the element")))
print(f"List is:{empty}")
visited=[]
for i in range(n):
    if empty[i] not in visited:
        count=0
        for j in range(n):
            if empty[i]==empty[j]:
                count+=1
        print(f"Frequency of {empty[i]} in the list is:{count}")
        visited.append(empty[i])