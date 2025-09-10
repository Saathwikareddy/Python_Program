name=str(input("Enter the string"))
positions=[]
for i in range(len(name)):
	count=0
	if name[i] not in positions:
		for j in range(len(name)):
			if name[j]==name[i]:
				count+=1

		positions.append(name[i])
		print(f"{name[i]}{count}",end='')