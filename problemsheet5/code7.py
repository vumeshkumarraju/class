#to check weather a nu,mber is harshad number or not

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will check wether your entered number is harshad or not.\n")
num=int(input("ENTER AN INTEGER = "))
num_copy=num
sum=0
while num!=0:
	dig=num%10
	sum=sum+dig
	num=int(num/10)
if num_copy%sum==0:
	print(num_copy," IS A HARSHAD NUMBER.")
else:
	print(num_copy," IS NOT A HARSHAD NUMBER.")
