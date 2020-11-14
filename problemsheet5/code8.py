#to check weather a bumber is pronic or not.

print("\n\t..........|| WELCOME TO THE PROGRAM ||.............")
print("we will chck wether your entered number is pronic or not.\n")
num=int(input("ENTER AN INTEGER = "))
k=0
i=1
fact=1
while fact<=num:
	fact=i*(i+1)
	if fact==num:
		print(i,'*',i+1," = ",fact)
		print(num," IS A PRONIC NUMBER.")
		k=2
	i+=1
if k==0:
	print(num," IS NOT A PRONIC NUMBER.")


