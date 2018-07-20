#call by reference in python


def printval(list):
	print("list before change=",list)
	list[3]=500
	print("list after change",list)

list =[10,20,30,40,50]
printval(list)
print("list outside=",list)


print("iterate list using for loop")
for i in list:
	print(i,end="\t")
	
