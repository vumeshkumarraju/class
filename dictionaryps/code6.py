#sumation of all the keys and values of the dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("PLEASE ENTER ONLY INTEGER VALUES FOR KEYS AND VALUES FOR THE DICTIONARY,\nWE WILL FIND THE SUMATION OF ALL THE KEYS AND VALUES(ITEMS). \n")
d={}
n=int(inout("ENTER THE NUMBER OF ITEMS YOU WANT TO ENTER IN THE DICTIONARY :- "))
for i in range(n):
    key=int(input("PLEASE ENTER THE KEY FOR ITEAM {} :- ".format(i+1)))
    value=int(input("PLEASE ENTER THE VALUE FOR ITEAM {} :- ".format(i+1)))
    d[key]=value
print("THE DICTIONARY :- ",d)
key_sum=0
value_sum=0
for j in d:
    key_sum=key_sum+j
    value_sum=value_sum+d[j]
print("THE SUM OF THE KEYS = ",key_sum)
print("THE SUM OF THE VALUES = ",value_sum)
print("\n....THE NET SUMATION OF ITEAMS = ",key_sum+value_sum)
    
