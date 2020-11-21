#dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("to find the square ..\n")
n=int(input("ENTER THE NUMBER TILL WHICH YOU WANT TO FIND THE SQUARE :- "))
square={}
for i in range(n+1):
	square[i]=i*i
print("THE LIST OF SQUARES OF THE INTEGER :- ",square)
