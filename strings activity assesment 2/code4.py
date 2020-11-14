#to check weather a string is present inside another

print("\n\t..........WELCOME TO THE PROGRAM............")
print("enter two strings we will check wether the sceond entered string is inside the first enteres string..\n")
string=input("enter your statement = ")
check_string=input("enter the string which is to find = ")
x=check_string in string
if x == True:
	print("\nYES,The '",check_string,"' is present inside the '",string,"'\n")
else:
	print("\nNO,The '",check_string,"' is not present inside the '",string,"'\n")