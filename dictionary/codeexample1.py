#dictionary

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
name=input("enter the name :- ")
student_dict={"Name":name}
n=int(input("enter the number of subjects :"))
total_mark=int(input("Enter the total marks of each subject = "))
result="<<..PASS..>>"
for i in range(1,n+1):
    sub=input("enter the name of subject {} :-".format(i))
    mark=int(input("enter the mark of {} :-".format(sub)))
    if mark<(0.3*total_mark):
        result="FAIL..!"
    student_dict[sub]=mark            #adding new iteams
if result=="FAIL..!":
    student_dict["Result"]=result
else:
    student_dict["Result"]=result
for a,b in student_dict.items():
    print(a," :- ",b)

#update the dictonary
print("INTIAL STUDENT DICTIONARY : ",student_dict)
update_sub=input("Enter the subject you want to update the marks : ")
if update_sub in student_dict:
    update_mark=int(input("ENTER THE MARK OF SUBJECT {} :-".format(update_sub)))
    student_dict.update({update_sub:update_mark})
    if update_mark<(0.3*total_mark):
        student_dict.update({"Result":"FAIL..!"})
    elif result!="<<..PASS..>>":
        student_dict.update({"Result":"<<..PASS..>>"})
    else:
        student_dict.update({"Result":"FAIL..!"})
else:
    print("the subject does not exist.")
print("the updated dictonary :",student_dict)

#pop function to remove iteam

print("INTIAL STUDENT DICTIONARY : ",student_dict)
remove_sub=input("enter the subject you want to remove from the list :- ")
if remove_sub in student_dict:
    student_dict.pop(remove_sub)
else:
    print(remove_sub,"does not exist in student dictionary.")
print("the updated dictonary after removing one iteam :",student_dict)

#popiteam to remove th last iteam.

print("\nINTIAL STUDENT DICTIONARY : ",student_dict)
student_dict.popitem()
print("the updated dictonary after doing popiteam :",student_dict)

#using del keywoard

print("\nINTIAL STUDENT DICTIONARY : ",student_dict)
delete_sub=input("enter the subject you want to remove from the list :- ")
if delete_sub in student_dict:
    del student_dict[delete_sub]
else:
        print(delete_sub,"does not exist in student dictionary.")
print("the updated dictonary after deleting one iteam :",student_dict)

#coping a dictionary using copy function
student_dict1=student_dict.copy()
print("\nthe orginal student dictionary :- ",student_dict)
print("the copied student dictionary :- ",student_dict1)

#copying using dict fuction

student_dict2=dict(student_dict)
print("\nthe orginal student dictionary :- ",student_dict)
print("the 2nd  copied student dictionary :- ",student_dict2)

#clear function
print("\nINTIAL STUDENT DICTIONARY : ",student_dict1)
print("\n clearing all the iteam from 1st copeid student dictonary.\n")
print("after clearing :-",student_dict1)

#deleting the whole dictionary

print("\nINTIAL STUDENT DICTIONARY(2nd copied) : ",student_dict2)
del student_dict2
print("\nafter deleting the 2nd copied student dictonary :- ",student_dict2)



