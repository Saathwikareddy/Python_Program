def bill():
    cno=int(input("Enter consumer no"))
    cname=input("Enter consumer name")
    pread=int(input("Enter present month reading"))
    lread=int(input("Enter last month reading"))
    totalunits=pread-lread
    return totalunits
x=bill()
if x>=1 and x<=50:
    Totalcost=x*3.80
    print(f"Total cost is:{Totalcost}")
elif x>=51 and x<=100:
    Totalcost=(50*3.80)+(x-50)*4.20
    print(f"Total cost is:{Totalcost}")
elif x>=101 and x<=200:
    Totalcost=(50*3.80)+(50)*4.20+(x-100)*5.10
    print(f"Total cost is:{Totalcost}")
elif x>=201 and x<=300:
    Totalcost=(50*3.80)+(50)*4.20+(100)*5.10+(x-150)*6.30
    print(f"Total cost is:{Totalcost}")
elif x>300:
    Totalcost=(50*3.80)+(50)*4.20+(100)*5.10+(150)*6.30+(x-200)*7.50
else:
    print("Invalid")

