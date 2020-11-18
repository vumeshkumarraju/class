#Number list

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("\nYOU CAN ENTER DIFFERENT NUMBERS FOR NUMBER LIST.")
x=int(input("ENTER HOW MANY NUMBERS YOU WANT TO ENTER IN THE LIST = "))
number_list=[]
for i in range(1,x+1):
	num=int(input("ENTER THE NUMBER {} :- ".format(i)))
	number_list.append(num)
print("\nTHE NUMBER LIST BEFORE ANY CHANGE :-",number_list)
number_list.sort()
print("\nTHE NUMBER LIST HAVING NUMBERS IN ASCENDING ORDER :-",number_list)
number_list.sort(reverse=True)
print("\nTHE NUMBER LIST HAVING NUMBERS IN DESCENDING ORDER :-",number_list)
even_number_list=[]
for i in number_list:
	if i%2==0:
		even_number_list.append(i)
print("\nTHE LIST OF EVEN NUMBERS FROM THE ABOVE NUMBER LIST :- ",even_number_list)
positive_number_list=[]
for i in number_list:
	if i>=0:
		positive_number_list.append(i)
print("\nTHE LIST OF POSITIVE NUMBERS FROM THE ABOVE LIST OF ITEAMS :- ",positive_number_list)


