#convert a list into dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will convert your entered list into a dictionary in which the half of the iteam as key and another half as its value.\n")
original_list=[]
dict={}
n=int(input("ENTER NUMBER OF INTEGERS YOU WANT TO ENTER IN THE LIST = "))
for i in range(n):
    number=int(input("ENTER THE INTEGER {} :- ".format(i+1)))
    original_list.append(number)
print("\nTHE ORIGINAL LIST :- ",original_list)
for j in original_list:
    temp=str(j)
    length=len(temp)
    half=length//2
    a=int(temp[0:half])
    b=int(temp[half:length])
    dict[a]=b
print("\nCONSTRUCTED DICTIONARY :- ",dict)
    
