#calculation of total marks and average marks and result as pass or fail

print("\n\t...........WELCOME..........\n")
print("please enter all the marks of class 12th out of 100 properly to find the proper result.\nALL THE BEST......\n")
sub_eng=float(input("ENTER THE MARKS OF ENGLISH = "))
assert sub_eng >=0 and sub_eng<=100
sub_math=float(input("ENTER THE MARKS OF MATH = "))
assert sub_math >=0 and sub_math<=100
sub_phy=float(input("ENTER THE MARKS OF PHYSICS = "))
assert sub_phy >=0 and sub_phy<=100
sub_chem=float(input("ENTER THE MARKS OF CHEMISTRY = "))
assert sub_chem >=0 and sub_chem<=100
sub_comp=float(input("ENTER THE MARKS OF COMPUTER SCIENCE = "))
assert sub_comp >=0 and sub_comp<=100
total_marks=sub_eng+sub_math+sub_phy+sub_chem+sub_comp
avg_marks=total_marks/5
if sub_eng>=50 and sub_math>=50 and sub_phy>=50 and sub_chem>=50 and sub_comp>=50:
	print("\n....CONGRATS...\nyou have passed your examination.")
else:
	print("\n!!!!!!YOU HAVE FAILED THE EXAMINATION.")
	print("BETTER LUCK NEXT TIME FOR YOUR EXAM.")
print("YOUR TOTAL MARKS = ",total_marks)
print("YOUR AVERAGE MARKS = ",avg_marks)






