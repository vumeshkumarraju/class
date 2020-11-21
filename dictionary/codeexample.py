#dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
student_dict={'Name': 'UMESH', 'ENGLISH': 94, 'MATH': 95, 'PHYSICS': 95, 'CHEMISTRY': 95, 'COMPUTER': 100, 'Result': '<<..PASS..>>'}

# accesing the iteams

n=student_dict['Name']
print(n,"\n")


for i in student_dict:           #accesing through loop
    x=student_dict.get(i)       #using get function in dictionary
    print(x)

# changing value

student_dict['ENGLISH']=90
student_dict['MATH']=98

# printing all the values

for j in student_dict:
    print(student_dict[j])
print("\n")

#acessing throgh the values function
for k in student_dict.values():
    print(k)
print("\n")

#to pront both key and values through item function

for x,y in student_dict.items():
    print(x," : ",y)
print("\n")

#to check if key exist or not

check=input("enter the key you want to check in the student dcitionary :- ")
if check in student_dict:
    print("THE KEY ",check," EXIST IN TEH STUDENT DICTIONARY.")
else:
    print("THE KEY ",check," DOES NOT EXIST IN TEH STUDENT DICTIONARY.")
print("\n")

#to check the length of dictionary
length=len(student_dict)
print("THERE ARE ",length," ITEAMS IN THE STUDENT DICTIONARY.")


