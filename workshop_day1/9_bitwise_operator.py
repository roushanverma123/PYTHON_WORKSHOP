''' & -bitwise and
    | -bitwise or
    ^ -bitwise xor
    << -bitwise leftshift 2 raise to the power bits shifted
    >> -bitwise rightshift 2 aise to the power bits shifted

    ones compliment (~) = -(number + 1)
    '''
a = int(input("enter first number"))
b = int(input("enter second number"))
c= a+b
print("c =",c)
print("yuppie we learned something new")

a=15
b=14

c= a&b
d= a|b
e= a^b
f= a<<2
g= a>>2
h= ~a

print(a,b,c,d,e,f,g,h)

print("formatt specifier")
print("a=%d b=%d" %(a, b))
