#showing pattern using while loop

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will show a pattern using integers.\n")
line=int(input("enter the number of lines = "))
i=line
while i>=1:
	j=0
	while j<=i:
		print(j,end=" ")
		j += 1
	print("\n")
	i -= 1