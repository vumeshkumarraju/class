#to check weather entered character is an alphabet

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will check wether your entered chacrcter is an alphabet.\n")
x=input("Enter an charcter :- ")
if (ord(x)>=65 and ord(x)<=90)or(ord(x)>=97 and ord(x)<=122):
	print("The character '",x,"' is an aplhabet.")
else:
	print("The character '",x,"' is not an aplhabet.")