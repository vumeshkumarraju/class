#showing pattern using for loop

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will show a pattern using integers using for loop.\n")
line=int(input("enter the number of lines = "))
for i in range(line,0,-1):
	for j in range(0,i+1):
		print(j,end=" ")
	print("\n")


