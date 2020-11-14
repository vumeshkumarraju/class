#encoding the data

print("\n\t.......WELCOME TO THE PROGRAM........")
print("your entered data will be encoded.\n")
data=input("enter the data :- ")
string=data
string=string.replace("a","5")
string=string.replace("b","+")
string=string.replace("c","$")
print("\nTHE ORIGINAL DATA :- ",data)
print("THE ENCODED DATA :- ",string,"\n") 


