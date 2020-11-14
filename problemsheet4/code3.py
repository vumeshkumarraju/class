#to check wether the year is leap year or not

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will check wether your entered year is leap year or not.")
yr=int(input("enter the year = "))
if (yr%4==0 and yr%100!=0) or yr%400==0:
	print(yr," year is a leap year.")
else:
	print(yr," year is not a leap year.")