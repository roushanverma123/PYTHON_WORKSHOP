#multiplication table using for loop

num=int(input("enter any number"))

for i in range(1,11):
	t = num * i
	print(num,"*",i,"=",t)

#using while
num= int(input("enter another no"))

i=1
while i<=10:
	t=num*i
	print(num,"*",i,"=",t)
	i +=1		