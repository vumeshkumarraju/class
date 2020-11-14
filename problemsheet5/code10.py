#prirnting a pattern

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will show a pattern as per your number of lines.\n")
line=int(input("ENTER THE NUMBER OF LINES = "))
print("\n\t.SHOWING YOU A PATTERN.\n")
for i in range(1,line+1):
	for j in range(1,i+1):
		print(i*j,end=' ')
	print("\n")
