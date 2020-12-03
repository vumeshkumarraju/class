#operations with two different numberss

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")

def sum_numbers(a,b):                               #addition
    print("\n\t......ADDITION......")
    print("{} + {} = {}".format(a,b,a+b))
def sub_numbers(a,b):                               #subtraction
    print("\n\t......SUBTRACTION......")
    print("{} - {} = {}".format(a,b,a-b))
def product_numbers(a,b):                               #multiplication
    print("\n\t......MULTIPLICATION......")
    print("{} * {} = {}".format(a,b,a*b))
def div_numbers(a,b):                               #division
    print("\n\t......DIVISION......")
    print("{} / {} = {}".format(a,b,a/b))
    
print("||........READ THE INSTRUCTION PROPERLY..........||")
print("ENTER TWO NUMBERS FOR VARIOUS ARITHMETIC OPERATION.")
print("\n\t1.ENTER 1 FOR ADDITION .\n\t2.ENTER 2 FOR SUBTRACTION .\n\t3.ENTER 3 FOR MULTIPLICATION .\n\t4.ENTER 4 FOR DIVISION .")
c1="yes"
while c1.lower()=="yes":
    n1=float(input("\nENTER THE 1ST NUMBER :- "))
    n2=float(input("ENTER THE 2ND NUMBER :- "))
    c2="yes"
    while c2.lower()=="yes":
        n=int(input("ENTER THE OPTION FOR YOUR FAVOURABLE ARITHMETIC OPERATION :- "))
        if n==1:
            sum_numbers(n1,n2)
        elif n==2:
            sub_numbers(n1,n2)
        elif n==3:
            product_numbers(n1,n2)
        elif n==4:
            div_numbers(n1,n2)
        else:
            print("\tPLEASE READ THE INSTRUCTION PROPERLY ")
            print("\n\t1.ENTER 1 FOR ADDITION .\n\tNTER 2 FOR SUBTRACTION .\n\t1.ENTER 3 FOR MULTIPLICATION .\n\tNTER 4 FOR DIVISION .")
            continue
        c2=input("\nENTER YES TO CHOSE ANOTHER OPTION FOR ARITHMETIC OPERATION WITH SAME NUMBERS IF NOT PRESS NO :- ")
    c1=input("\nENTER YES TO ENTER TWO DIFFERENT NUMBERS FOR ARITHMETIC OPERATIONS IF NOT PRESS NO :- ")
            
