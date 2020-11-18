#factorial of a number
print("\nwelcome to the program")
print("we are going to find the factorial of your inputed number.\n")
n = int(input("enter the number="))
i=n
fact=1
print("THE FACTORIAL OF ",n,":-")
while i>1:
	fact=fact*i
	print(i,end=" x ")
	i-=1
print("1 = ",fact)
	