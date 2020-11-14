#to count the number of upper case letters and lower case letters and numbers of digits

print("\n\t......WELCOME........")
print("lets count number of upper case and lower case alphabets and number of digits present in your entered string.\n")
string=input("enter the string :- ")
i=0
count_lower=0
count_upper=0
count_digit=0
while i<len(string):
	if string[i].islower() == True:
		count_lower+=1
	elif string[i].isupper() == True:
		count_upper+=1
	elif string[i].isdigit() == True:
		count_digit+=1
	i+=1
print("NUMBER OF LOWER CASE ALPHABETS IN YOU ENTERED STRING = ",count_lower)
print("NUMBER OF UPPER CASE ALPHABETS IN YOU ENTERED STRING = ",count_upper)
print("NUMBER OF DIGITS IN YOU ENTERED STRING = ",count_digit)








