#function body and definition and loop
def hello(s):
	i=1
	while i <= s:
		print(i,end=" ")
		i+= 1
#to call the function
s = int(input("enter last number"))
hello(s)
