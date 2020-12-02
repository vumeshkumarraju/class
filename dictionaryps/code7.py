#multiplication of all the keys and values of the dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("PLEASE ENTER ONLY INTEGER VALUES FOR KEYS AND VALUES FOR THE DICTIONARY,\nWE WILL FIND THE MULTIPLICATION OF ALL THE KEYS AND VALUES(ITEMS). \n")
d={}
n=int(input("ENTER THE NUMBER OF ITEMS YOU WANT TO ENTER IN THE DICTIONARY :- "))
for i in range(n):
    key=int(input("PLEASE ENTER THE KEY FOR ITEAM {} :- ".format(i+1)))
    value=int(input("PLEASE ENTER THE VALUE FOR ITEAM {} :- ".format(i+1)))
    d[key]=value
print("THE DICTIONARY :- ",d)
key_product=1
value_product=1
for j in d:
    key_product=key_product*j
    value_product=value_product*d[j]
print("THE PRODUCT OF THE KEYS = ",key_product)
print("THE PRODUCT OF THE VALUES = ",value_product)
print("\n....THE NET MULTIPLICATION OF ITEAMS = ",key_product*value_product)
    
