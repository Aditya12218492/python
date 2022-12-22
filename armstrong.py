x=int(input())
y=x
cubesum=0
while x !=0:
    a=x%10
    cubesum +=a*a*a
    x=int(x/10)
if y==cubesum:
    print("cubesum") 
else:
    print("not amstrong")