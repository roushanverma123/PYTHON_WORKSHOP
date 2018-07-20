#variable length argument function
def printval(x,*a):
	#*a is of tuple type
	print("first = ",x)
	print(type(x),type(a))

	for y in a:
		print(y)



printval(10)
printval(100,200,300)
printval(-10,-20,-30,-40,-50)
