#find the type of triangle
print("\twelcome to the progarm")
print("we will find the type of triangle by your input angle")
print("you ust input the angle of triangle in degree\n")
a = int(input("enter the first angle ="))
b = int(input("enter the second angle ="))
c = int(input("enter the third angle ="))
sum = a+b+c
if sum == 180 and a!=0 and b!=0 and c!=0:
	if a<90 and b<90 and c<90:
		print("AS PER YOUR INPUTS OF ANGLE THE TRIANGLE IS ACUTE ANGLE TRIANGLE.")
	elif a==90 or b==90 or c==90:
		print("AS PER YOUR INPUTS OF ANGLE THE TRIANGLE IS RIGHT ANGLE TRIANGLE.")
	else:
		print("AS PER YOUR INPUTS OF ANGLE THE TRIANGLE IS OBTUSE ANGLE TRIANGLE.")
else:
	print("sorry!!!\nyou have entered wrong angles,the sum of the angles must be 180 degree and angle must have a proper value.")