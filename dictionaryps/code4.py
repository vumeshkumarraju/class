#to concaneate dictonaries

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("YOU EENTER ITEAMS AND NUMBER OF DICTIONARY WE WILL MERGE THEM TO A SINGLE DICTIONARY.\n")
num=int(input("ENTER NUMBER OF DICTIONARY :- "))
merge_dict={}
for i in range(num):
    d={}
    num_iteam=int(input("ENTER NUMBER OF ITEAS IN THE DICTIONARY :- "))
    for j in range(num_iteam):
        key=input("enter the key :- ")
        value=input("enter the value :- ")
        d[key]=value
    print("THE DICTIONARY {} :- ".format(i+1),d)
   #merging
    for k in d:
        merge_dict[k]=d[k]
print("THE CONCANEATION OF DICTONARIES :- ",merge_dict)
    

