def compatible(a,b):
    return (a<=b+1) and (2*a>b-2);

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
print(['NO','YES'][compatible(a[0],b[1]) or compatible(a[1],b[0])])