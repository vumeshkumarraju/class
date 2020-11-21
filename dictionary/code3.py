#dictionary of squares part2

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("to find the square ..\n")
n=int(input("ENTER THE NUMBER TILL WHICH YOU WANT TO FIND THE SQUARE :- "))
square_dict={i:i*i for i in range(n+1)}
print("THE SQUARES OF INTEGERS :- ",square_dict)
