a=input()
a=" ".join(a)
a=a.split()
suma=0
entra=0
for k in range (len(a)):
        if a[k]==a[k].upper():
                suma=suma+1
        else:
                if k==0:
                        entra=1
                        
if  suma==len(a) or (suma==(len(a)-1) and entra==1):
        if a[0]==a[0].upper():
                a[0]=a[0].lower()
        else:
                a[0]=a[0].upper()
        for k in range (1,len(a)):
                a[k]=a[k].lower()
        mensaje="".join(a)
else:
        mensaje="".join(a)
print(mensaje)