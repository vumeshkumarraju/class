#to check the item already exists in the dictionary or not

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("WE WILL CHECK WEATHER YOUR ENTERED THING IS PRESENT IN THE KEY OF THE DICTIONARY.\n")
student_dict={'Name': 'UMESH', 'ENGLISH': 94, 'MATH': 95, 'PHYSICS': 95, 'CHEMISTRY': 95, 'COMPUTER': 100, 'Result': '<<..PASS..>>'}
check_key=input("ENTER THE KEY YOU WANT TO CHECK :- ")
print("\n")
if check_key in student_dict:
    print(check_key," alerady exists in the dictionary.")
else:
    print("!!! ",check_key," doesn't exist in the dictionary.")
