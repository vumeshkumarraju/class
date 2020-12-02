#to remove the duplicate items forom the dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("PLEASE ENTER THE KEYS AND VALUES FOR THE DICTIONARY\n")
n=int(input("PLEASE ENTER THE NUMBER OF ITEMS FOR DICTIONARY :- "))
d={}
for i in range(n):
    key=input("ENTER THE KEY OF THE ITEM :- ")
    value=input("ENTER THE VALUE OF ITEM :- ")
    d[key]=value
print("\nREMOVING THE ITEMS HAVING DUPLICATING VALUES .")
d1=d.copy()
for x,y in d1.items():
    check=y
        for j in d:
            if check==d[j]:
                d.pop(check)    
print("THE DICTIONARY :- ",d)
