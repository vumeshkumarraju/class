#showing pattern using while loop

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will show a pattern as per your requirment of lines but it must not exceed 6.\n")
line=int(input("enter the number of lines = "))
a=65
i=1
while i<=line:
	j=1
	while j<=i:
		print(chr(a),end=" ")
		j += 1
		a += 1
	print("\n")
	i += 1