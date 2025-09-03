cno=int(input("Enter consumer no"))
cname=int(input("Enter consumer name"))
pread=int(input("Enter present month reading"))
lread=int(input("Enter last month reading"))
totalunits=pread-lread
currentbill=totalunits*3.80
print(f"customer number: {cno} \n customer name:{cname} \n PMR:{pread} \n LMR:{lread} \n Total units:{totalunits} \n Current bill: {currentbill}")