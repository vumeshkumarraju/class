#list of different iteams

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("\nYOU CAN ENTER DIFFERENT ITEAMS FOR THE LISTS.")
x=int(input("ENTER HOW MANY ITEAMS YOU WANT TO ENTER IN LISTS = "))
string_number_list=[]
iteam_not_added=[]
k=1
while k <= x:
	iteam=input("ENTER THE ITEAM {} :- ".format(k))
	if iteam.isdigit()==True:
		if int(iteam)%2==0 and int(iteam)>=100 and int(iteam)<=800:
			string_number_list.append(int(iteam))
		else:
			iteam_not_added.append(int(iteam))
	else:
		vowels=['a','e','i','o','u','A','E','I','O','U']
		if iteam[0] in vowels:
			string_number_list.append(iteam)
		else:
				iteam_not_added.append(iteam)
	k+=1
print("THE LIST :- ",string_number_list)
print("\n||.....",iteam_not_added," CAN NOT BE ENTERED IN THE ABOVE LIST DUE TO THESE CONSTRAINTS ......||")
print("ONLY STRINGS STARTING WITH VOWELS,POSITIVE INTEGERS,EVEN NUMBERS,NUMBERS BETWEEN 100 TO 800 ARE ADDED TO THE LISTS.")

			




