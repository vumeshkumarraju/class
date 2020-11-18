#make a list of car

import copy
print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("YOU CAN ENTER THE CAR NAMES FOR THE CAR LIST\n")
list_of_cars=[]
x=int(input("ENTER THE NUMBER OF CARS IN THE LIST YOU WANT TO ENTER = "))
for i in range(1,x+1):
	car=input("ENTER THE NAME OF CAR {} :- ".format(i))
	list_of_cars.append(car)
print("\n THE CAR LIST :- ")
print("THE LIST OF CARS BEFORE ANY CHANGES :- ",list_of_cars)
list_of_cars_ascending=copy.copy(list_of_cars)
list_of_cars_ascending.sort(key=str.lower)
print("\nTHE LIST OF CARS IN THE ASCENDING ORDER :- ",list_of_cars_ascending)
list_of_cars_descending=copy.copy(list_of_cars)
list_of_cars_descending.sort(reverse=True,key=str.lower)
print("\nTHE LIST OF CARS IN THE DESCENDING ORDER :- ",list_of_cars_descending)