#calculating a budget for a computer lab
print("\n\t\t........WELCOME........")
print("\t...calculate the budget of your lab...\n")
print("please enter proper quantity and price for the acurrate calculation.")
print("\nNow input all the cost.\n")
comp=float(input("please enter the cost of each computer :- "))
table=float(input("please enter the cost of each computer table :- "))
chair=float(input("please enter the cost of each chair :- "))
worker=float(input("please enter the wages of labour for working an hour :- "))
print("\nNow input the quantity and working hour.\n")
qty_comp=int(input("please enter the number of computer systems :- "))
qty_table=int(input("please enter the number of tables :- "))
qty_chair=int(input("please enter the number of chairs :- "))
hr_worker=int(input("please enter the number of hours worked :- "))
cost_comp=comp*qty_comp
cost_furniture=(table*qty_table)+(chair*qty_chair)
cost_worker=worker*hr_worker
budget=cost_comp+cost_furniture+cost_worker
print("\n\t.........BUDGET CALCULATION.........")
print("THE TOTAL COST FOR COMPUTER SYSTEM :- Rs.",cost_comp,"\-")
print("THE TOTAL COST FOR TABLE :- Rs.",cost_furniture,"\-")
print("THE TOTAL COST FOR WORKER :- Rs.",cost_worker,"\-\n")
print("\tTHE TOTAL COST FOR THE LAB :- Rs.",budget,"\-\n") 



















