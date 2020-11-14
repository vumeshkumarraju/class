#the sum of all trhe digits of a given number
print("\n\t..WELCOME TO THE PROGRAM..")
print("we will find the sum of all the digits of the inputed number.\n")
num=int(input("enter the number="))
copy=num
lastd=copy%10
copy1=str(int(num/10))
sum=0
while copy!=0:
	a=copy%10
	copy=int(copy/10)
	sum=sum+a
print("the sum of the digits ",end=': ')
for i in copy1:
	print(i,end=' + ')
print(lastd,sum,sep=' = ')









