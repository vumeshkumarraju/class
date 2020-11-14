#printing the pattern with strings
print("\n\t.....WELCOME TO THE PROGRAM......")
print("we will show pattern with alphabets from a to the alphabet you have entered")
alp=input("enter an alphabet=")
i=97
x=ord(alp)
while i<=x:
	j=97
	while j<=i:
		print(chr(i),end=" ")
		j+=1
	print("\n")
	i+=1
i=97
while i<=x:
	j=97
	while j<=i:
		print(chr(j),end=" ")
		j+=1
	print("\n")
	i+=1
i=97
while i<=x:
	j=97
	while j<=i:
		if i%2==0:
			print(i-96,end=" ")
		else:
			print(chr(i),end=" ")
		j+=1
	print("\n")
	i+=1