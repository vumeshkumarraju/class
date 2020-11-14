#showing pattern using for loop

print("\n\t.......WELCOME TO THE PROGRAM.........")
print("we will show a pattern as per your requirment of lines but it must not exceed 6.\n")
line=int(input("enter the number of lines = "))
a=65
for i in range(1,line+1):
	for j in range(0,i):
		print(chr(a),end=" ")
		a += 1
	print("\n")

