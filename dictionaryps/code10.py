#combine two dictionary having values for common key

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("WE WILL COMBINE YOUR TWO DICTIONARY BY ADDING VALUES FOR COMMON KEYS.\n")
print("PLEASE ENTER ITEMS FOR TWO DICTIONARY AND VALUES MUST BE INTEGERS.\n")
d1={}
d2={}
for i in range(2):
    n=int(input("ENTER THE NUMBER OF ITEMS IN DICTIONARY {} :- ".format(i+1)))
    for x in range(n):
        key=input("ENTER THE KEY FOR item {} :- ".format(x+1))
        value=int(input("ENTER THE VALUE FOR {} OF item {} :- ".format(key,x+1)))
        if i==0:d1[key]=value
        else:d2[key]=value
print("THE DICTIONARY {} :- ".format(1),d1)
print("THE DICTIONARY {} :- ".format(2),d2)
temp=0
d_combine={}
for j in d1:
    for k in d2:
        if j==k:
            d_combine[j]=d1[j]+d2[k]
            temp+=1
print("THE COMBINED DICTIONARY :- ",d_combine)
if temp==0:
    print("THERE IS NOT ANY COMMON KEYS IN BOTH THE DICTIONARY......!")
