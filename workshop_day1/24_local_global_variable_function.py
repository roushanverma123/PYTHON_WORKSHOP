#local and global variable using function
def printval(a,b):
	global total
	total= a+b

printval(10,20)
print("total=",total)