#printing a pattern using umbers

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will show a pattern as your entered number of lines.\n")
line=int(input("ENTER NUMBER OF LINES = "))
for i in range(1,line+1):
	for j in range(line,0,-1):
		if i==j:
			print('*',end=" ")
		else:
			print(j,end=" ")
	print("\n")
	