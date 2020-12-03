#examples for function

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("\n")
def swap_num(a,b):
    c=a
    a=b
    b=c
    print("\nINSIDE FUNCTION :\n a :- {}\nb :- {}".format(a,b))
a=int(input("enter a = "))
b=int(input("enter b = "))
print("\nBEFORE FUNCTION CALL :\n a :- {}\nb :- {}".format(a,b))
swap_num(a,b)
print("\nBEFORE FUNCTION CALL :\n a :- {}\nb :- {}".format(a,b))
