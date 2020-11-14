num=int(input("enter the number="))
factor=2
k=0
if num>2:
	while factor<num:
		if num%factor==0:
			k+=1
			print("the number is not prime")
			break
		factor+=1
	if k==0:
		print("the number is a prime.")
elif num==2:
	print("2 is prime.")
elif num==1:
	print("1 is neither prime nor composite.")
elif num==0:
	print("0 is neither prime or composite.")  