for i in range(1,10):
	print(i,end=" ")
print("\nreverse\n")

for i in range(10,0,-1):
	print(i,end=" ")


print("\nstep index\n")
for i in range(1,11,2):
	print(i,end=" ")


print("\nnested for")
#nested for loop
for i in range(1,3):
	for j in range(1,3):
		if i == j:
			print(i,j)
		else:
			break
print(i,j)









