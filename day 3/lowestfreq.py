name=str(input("Enter a string:"))
positions=[]
count1=10000
for i in range(len(name)):
	count2=0
	if name[i] not in positions:
		for j in range(len(name)):
			if name[i]==name[j]:
				count2+=1
		positions.append(name[i])
		if count2<count1:
				count1=count2
				character1=name[i]
print(f"Lowest frequency is for {character1}:{count1}")