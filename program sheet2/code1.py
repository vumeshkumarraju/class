#total number of even numbers and odd numbers
print("\t..WELCOME TO THE PROGRAM..")
print("we will find number of even numvers and odd numbers in a given range of number.\n")
a=int(input("enter the starting number of range="))
b=int(input("enter the ending number of range="))
i=a
count_odd=0
count_even=0
while i<=b:
	if i%2 == 0:
		count_even += 1
	else:
		count_odd += 1
	i+=1
print("\nTHERE ARE ",count_even ," EVEN NUMBERS IN THE RANGE OF ",a," and ",b,".")
print("THERE ARE ",count_odd ," ODD NUMBERS IN THE RANGE OF ",a," and ",b,".")








	