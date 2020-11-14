#to count the number of vowels in an entered string.

print("\n\tWELCOME")
print("we will count the number of vowels present in the entered string.\n")
string = input("enter a string :- ")
sum=0
counta=0
counte=0
counti=0
counto=0
countu=0
i=0
while i < len(string):
	if string[i]=='a' or string[i]=='A':
		counta+=1
	elif string[i]=='e' or string[i]=='E':
		counte+=1
	elif string[i]=='i' or string[i]=='I':
		counti+=1
	elif string[i]=='o' or string[i]=='O':
		counto+=1
	elif string[i]=='u' or string[i]=='U':
		countu+=1
	i+=1
sum=counta+counte+counti+counto+countu
print("TOTAL NUMBER OF a = ",counta)
print("TOTAL NUMBER OF e = ",counte)
print("TOTAL NUMBER OF i = ",counti)
print("TOTAL NUMBER OF o = ",counto)
print("TOTAL NUMBER OF u = ",countu)
if sum==0:
	print("\nTHERE IS NO VOUWEL IN YOUR ENTERED STRING.\n")
else:
	print("\nTHERE ARE ",sum," VOWELS IN THE STRING.\n")