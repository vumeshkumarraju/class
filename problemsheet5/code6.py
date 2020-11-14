#to show all the disarium number in a given range

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will print all the disarium numbers in your entered range.")
a=int(input("enter the starting range = "))
b=int(input("enter the ending range = "))
print("THE DISARIUM NUMBERS BETWEEN ",a," AND ",b,end=" ARE :-")
for x in range(a,b+1):
	num=x
	count=0
	sum=0
	num1=num
	while num1!=0:
		count+=1
		num1=int(num1/10)
	for i in range(count,0,-1):
		dig=num%10
		sum=sum+dig**i
		num=int(num/10)
	if(sum==x):
		print(x,end=" ")

