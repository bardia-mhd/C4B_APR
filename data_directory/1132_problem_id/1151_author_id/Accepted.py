n=int(input())
c=0
if n%4==0 or n%7==0 or n%47==0 or n%74==0 or n%447==0 or n%474==0 or n%477==0 or n%747==0 or n%774==0:
    c=1
    print('YES')
n=str(n)
if c==0:
    if n.count('4')+n.count('7')==len(n):
        print('YES')
    else:
        print('NO')