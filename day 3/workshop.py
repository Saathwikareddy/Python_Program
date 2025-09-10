list=[]
n=int(input("Enter the number of lists"))
for i in range(n):
    x=int(input(f"Enter the number of attendees on day {i+1}:"))
    for j in range(x):
        list.append(input("Enter the email id:"))
print(list)
set1=set(list)
print(f"Total number of unique attendees in workshop:{len(set)}")
print(f"List of attendees who attended all three days")     
print(set1)
for i in range(len(list)):
    count=0
    for j in range(len(list)):
        if list[i]==list[j]:
            count+=1
    if count==1:
        print(f"{list[i]} attended only once")


