n=int(input())
if n%7==1 :
    max = 1+2*((n-1)//7)
    min = 2*((n-1)//7)
elif n%7==2 :
    max = 2+2*((n-2)//7)
    min = 2*((n-2)//7)
elif n%7==3 :
    max = 2+2*((n-3)//7)
    min = 2*((n-3)//7)
elif n%7==4 :
    max = 2+2*((n-4)//7)
    min = 2*((n-4)//7)
elif n%7==5 :
    max = 2+2*((n-5)//7)
    min = 2*((n-5)//7)
elif n%7==6 :
    max = 2+2*((n-6)//7)
    min = 2*((n-6)//7)+1
elif n%7==0 :
    max = 2*((n)//7)
    min = 2*((n)//7)
print (min,max)