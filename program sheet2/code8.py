#check wether a number is palindrome or not
print("\n\t...WELCOME...")
print("we will check weather your inputed number is a palindrome or not.\n")
num=int(input("enter the number = "))
print("Let's check the number wether palindrome or not.")
copy1=num
new_num=0
while copy1!=0:
	rem=copy1%10
	new_num=new_num*10 + rem
	copy1=int(copy1/10)
print("THE REVERSE NUMBER IS = ",new_num)
if num == new_num:
	print("THE ENTERED NUMBER IS A PLINDROME")
else:
	print("THE ENTERED NUMBER IS NOT A PALINDROME.")
	







