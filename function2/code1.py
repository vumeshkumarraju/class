#function

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("PLEASE ENTER THE INTEGERS FOR THE LIST.\n")
list_numbers=[]
num=int(input("ENTER NUMBER OF INTEGERS IN THE LIST :- "))
for i in range(num):
    item=int(input("ENTER THE INTEGER {} = ".format(i+1)))
    list_numbers.append(item)

def ascending(l):
    l.sort()
    print("SORTING THE LSIT IN ASCENDING ORDER :- ",l)
def descending(l):
    l.sort(reverse=True)
    print("SORTING OF THE LIST IN DESCENDING ORDER :-",l)

i=0
print("\n..PLEASE SELECT 1 FOR SORTING IN ASCENDING ORDER AND 2 FOR DESCENDING ORDER...\n")
while i<1:
    n=int(input("PLEASE ENTER YOUR OPTION :- "))
    if n==1:
        ascending(list_numbers)
        i+=1
    elif n==2:
        descending(list_numbers)
        i+=1
    else:
        print("PLEASE SECLECT PROPER OPTION. \nSELECT 1 FOR SORTING IN ASCENDING ORDER AND 2 FOR DESCENDING ORDER.")
        
