#dictionay

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will make a number dictonary from you entered values.\n")
n=int(input("PLEASE ENTER HOW MANY NUMNBERS YOU WANT TO ENTER IN THE DICTIONARY :- "))
number_dict={}
for i in range(1,n+1):
	number=input("ENTER THE NUMBER {} = ".format(i))
	number_dict[i]=number
print("THE NUMBER DICTIONARY :- ",number_dict)