def lucky(n):
    mes="YES"
    while((n>=1)and(mes=="YES")):
        ld=n%10
        if((ld==7)or(ld==4)):
            mes="YES"
            n=n//10
        else:
            mes="NO"
            n=-1
    return mes
def main(n):
    if (lucky(n)=="YES"):
        MESS="YES"
    else:
        for i in range(1,n+1):
            MESS="YES"
            if((lucky(i)=="YES")and(MESS=="YES")):
                if(N%i==0):
                    MESS="YES"
                else:
                    MESS="NO"
                    
    return MESS
N=int(input())
print(main(N))