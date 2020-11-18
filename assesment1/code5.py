#fibonacci series
print("\twelcome to the program")
print("we are going to find the fibonancy series as per your input number of terms\n")
x=0
y=1
n = int(input("enter the term till which you want to find the fibonancy series="))
i=3
print(x,y,sep=',',end=',')
while i<=n:
	sum=x+y
	x=y
	y=sum
	if i<n:
		print(sum,end=',')
	else:
		print(sum)
	i +=1
print("here is your fibonacci series")
 