a=input()
z=1
a=a.split(' ')
lista=list(map(int,a))

contador=0
k=lista[0]
t=lista[-1]
b=lista[1]
n=lista[-2]
while z<=t:
    z=k*z+b
    contador+=1
formula=n-contador+1
if formula<0:
    print("0")
else:
    print(formula)