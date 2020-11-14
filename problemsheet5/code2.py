#volume of cylinder

import math
print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will evaluate the volume for you cylinder.\n")
print("enter the values of height and radius in centimetres.")
height=int(input("ENTER THE HEIGHT OF YOUR CYLINDER :- "))
radius=int(input("ENTER THE RADIUS OF BASE OF THE CYLINDER :- "))
vol=math.pi*(radius**2)*height
print("\nTHE VOLUME OF YOUR CYLINDER IS :- ",vol," cube cm")
