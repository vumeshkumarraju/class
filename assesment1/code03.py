#to print multiples of a given number
print("\nwelcome to the program")
print("we are going to print the multiples of your inputed number\n")
x = int(input("enter the number="))
print("how many multiples of ",x," do you want",end='')
n = int(input(":-"))
i=1
a=x
print("the ",n," numbers of multiples of ",x," are :-")
while i<=n:
	if a%x==0:
		print(a,end=' ')
		i+=1
	a+=1
	
