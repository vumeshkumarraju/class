#print the sum of any 5 random number using random function
print("\n\t...WELCOME TO THE PROGRAM...")	
print("system will generate five random number in your range and will show you the number and also the sum.\n")
a=int(input("enter the starting number of the range="))
b=int(input("enter the ending number of the range="))
sum=0
i=1
print("\nLET'S SEE THE FIVE NUMBER AND THE SUM\n")
import random
print("the sum of the random numbers",end=" : ")
while i<=5:
	number=random.randrange(a,b)
	sum=sum+number
	if i!=5:
		print(number,end=' + ')
	else:
		print(number,end=' = ')
	i += 1
print(sum)








