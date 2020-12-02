#write description

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("sorting the iteams in dictionary\n")
d={}
n=int(input("ENTER THE NUMBER OF ITEAMS :- "))
for i in range(n):
    key=int(input("ENTER THE KEY = "))
    value=int(input("ENTER THE VALUE = "))
    d[key]=value
print("DICTIONARRY BEFORE SORTED :- ",d)
l=list(d.items())
l.sort()
d=dict(l)
print("DICTIONARY SORTED IN ASCENDING ORDER BY VALUE :- ",d)
l.sort(reverse=True)
d=dict(l)
print("DICTIONARY SORTED IN DSCENDING ORDER BY VALUE :- ",d)
