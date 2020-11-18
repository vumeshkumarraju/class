#calculating the area of circle and rectangle and compare it


print(".......welcome to the program........")
print("you can find the area of circle and rectangle by inputs")
radius = int(input("enter the radius :-"))
area1 = (22/7)*radius*radius
print("the rear of the circle =",area1)
length = int(input("enter the length of the rectangle ="))
breadth = int(input("enter the breadth of the rectangle ="))
area2 = length*breadth
print("the area of the rectangle =",area2)
	
if area1>area2:
	print(" THE AREA OF THE CIRCLE IS GREATER THAN THE AREA OF THE RECTANGLE.")
elif area2>area1:
	print(" THE AREA OF THE RECTANGLE IS GREATER THAN THE AREA OF THE CIRCLE.")
else:
	print(" THE AREA OF THE RECTANGLE IS EQUAL TO THE AREA OF THE CIRCLE.")