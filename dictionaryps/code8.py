#FIND THE MAXIMUM AND MINIMUM VALUES

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("PLEASE ENTER INTEGERS IN THE ITEMS OF YOUR DICTIONARY,\nWE WILL FIND OUT THE MAXIMU AND MINIMUM VALUES OUT OF THE DICTIONARY.")
d={}
n=int(input("ENTER THE NUMBER OF ITEMS YOU WANT TO ENTER IN THE DICTIONARY :- "))
for i in range(n):
    key=int(input("PLEASE ENTER THE KEY FOR ITEAM {} :- ".format(i+1)))
    value=int(input("PLEASE ENTER THE VALUE FOR ITEAM {} :- ".format(i+1)))
    d[key]=value
print("THE DICTIONARY :- ",d)
l=list(d.values())
print(l)
max=l[0]
min=l[0]
for i in l:
    if i>max:
        max=i
    if i<min:
        min=i
print("THE MAXIUM VALUE IN THE DICTIONARY :- ",max)
print("THE MINIMUM VALUE IN THE DICTIONARY :- ",min)
