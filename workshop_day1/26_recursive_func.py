#recursive function in python 
#a function which call itself
#recursion implemented using stack
#STACK works on FILO or LIFO (Last in first out/first in last out ) mechanism

def factor(n):
	if n<0:
		print("enter +ve no")
		exit(0)
	
	elif n == 0 or n == 1:
		return 1
	else:
		return n*factor(n-1)

num =int(input("enter any number"))
print("factorial= ",factor(num))