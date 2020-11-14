#to print the string in a different manner

print("\n\t.......WELCOME TO THE PROGRAM.........")
string=input("Enter a string :- ")
if len(string)>=7:	
	new_string=string[0:7]+string[len(string)-2:]
	print("The changed string is :- ",new_string)
else:
	print("string size is not sufficient.")




