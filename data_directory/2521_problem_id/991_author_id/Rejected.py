n=int(input())
a=2**(n-1)-1
i=0
while int(bin(2**(n-1)+i).replace("b","0"))<=n:
    i+=1
print(a+i)