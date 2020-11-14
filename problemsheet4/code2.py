#to check weather a number is prime or not

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will check wether your entered number is prime or not.\n")
x=int(input("Enter an integer = "))
if x==1:
	print("1 is neither prime nor composite.")	
else:
	for i in range(2,x):
		if x%i==0:
			print("The number ",x," is  not a prime number.")
			break
	else:
		print("The number ",x," is a prime number.")