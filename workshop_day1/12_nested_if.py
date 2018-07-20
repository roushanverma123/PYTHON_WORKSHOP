#nested if statement
a=int(input("enter 1st no"))
b=int(input("enter 2nd no"))
c=int(input("enter 3rd no"))


if a>b:
	if a>c:
		print("A is greater")
	else:
		print("c is greater ")
elif b>c:
	print("b is greater")
elif a==b==c:
	print("all are equal")
else:
	print("c is greater")



