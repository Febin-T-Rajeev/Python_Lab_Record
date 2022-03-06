s_year=int(input("Enter the starting year:"))
e_year=int(input("Enter the ending year:"))

print("The Leap years from ",s_year," to ",e_year," are : ")
for i in range(s_year,e_year+1):
    if((i%4==0 and i%100!=0) or (i%400 == 0)):
        print(i,end=" ")
    

