#to count all the characters except digits and alphabets
print("\n\t......WELCOME........")
print("lets count number of special characters except the alphabets and digits.\n")
string=input("enter the string :- ")
count=0
i=0
while i<len(string):
	if (ord(string[i])>=32 and ord(string[i])<=47)or (ord(string[i])>=58 and ord(string[i])<=63):
		count+=1
	i+=1
print("THERE ARE ",count," SPECIAL DIGITS PRESENT IN YOUR ENTERES STRING EXCEPT ALPHABETS AND DIGITS.")





