n=int(input(""))
L=input("")
cont=0
k=0
while(k<n-1):
    if(L[k]!=L[k+1]):
        break
    else:
        cont+=1
    k+=1
print(cont)