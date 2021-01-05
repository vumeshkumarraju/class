#to sort a list of numbers and store in files

#selection sorting for ascending order

def asc(ls):
	for i in range(n-1):
		#min value index
		mvi=i
		for j in range(i,n):
			if ls[j]<ls[mvi]:
				mvi=j
		ls[i],ls[mvi]=ls[mvi],ls[i]
	return ls

# selection sorting for descending order
def desc(ls):
	for i in range(n-1):
		# max value index
		mvi=i
		for j in range(i,n):
			if ls[j]>ls[mvi]:
				mvi=j
		ls[i],ls[mvi]=ls[mvi],ls[i]
	return ls


print("\n\t..........||WELCOME TO THE PROGRAM||..............\n")
print("PLEASE ENTER INTEGERS TO SORT AND WE WILL STORE IT IN A FILE.\n")
n=int(input("PLEASE ENTER THE NUMBER OF INTEGERS YOU WANT TO ENTER :-"))
list_numbers=[]
for i in range(n):
	a=int(input("ENTER THE INTEGER {} :- ".format(i+1)))
	list_numbers.append(a)
print("\nYOUR NUMBER LIST :-")
print(list_numbers)

asc_list=asc(list_numbers).copy()
desc_list=desc(list_numbers).copy()
print("\nYOUR NUMBER LIST AFTER SORTING IN ASCENDING ORDER:-")
print(asc_list)
print("\nYOUR NUMBER LIST AFTER SORTING IN DESCENDING ORDER:-")
print(desc_list)

#storing in files
f=open("ascending_numbers.txt","w")
g=open("descending_numbers.txt","w")
even=open("even_numbers.txt","w")
odd=open("odd_numbers.txt","w")
f.write("\t: NUMBER IN ASCENDING ORDER :\n")
g.write("\t: NUMBER IN DESCENDING ORDER :\n")
even.write("\t: EVEN NUMBERS :\n")
odd.write("\t: ODD NUMBERS :\n")
for i in range(n):
	f.write(str(asc_list[i])+"\n")
	g.write(str(desc_list[i])+"\n")
	if asc_list[i]%2==0:
		even.write(str(asc_list[i])+"\n")
	else:
		odd.write(str(asc_list[i])+"\n")
f.close()
g.close()
even.close()
odd.close()
		
