#to check weather a number is disarium or not

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will check weather your entered number is disarium or not.")
num=int(input("ENTER AN INTEGER = "))
count=0
sum=0
num1=num
num_check=num
while num1!=0:
	count+=1
	num1=int(num1/10)
for i in range(count,0,-1):
	dig=num%10
	sum=sum+dig**i
	num=int(num/10)
print("the sum of the digits to the power to their places = ",sum)
if sum==num_check:
	print(num_check," is a disarium number.")
else:
	print(num_check," is not a disarium number.")

