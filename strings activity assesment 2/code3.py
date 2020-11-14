#to check weather the string is palindrome or not

print("\n\t......WELCOME......")
print("we will check your entered string is palindrome or not.\n")
string=input("enter the string :- ")
rev_string=string[::-1]
if string==rev_string:
	print("\n.....Your entered string is palindrome.....\n")
else:
	print("\n!!!!your entered string is not palindrome.")
	print("the reverse string is :- ",rev_string)

