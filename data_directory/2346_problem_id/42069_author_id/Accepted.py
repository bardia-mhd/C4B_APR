a,b,c,d=map(int,input().split())
#all pairs
#a b c
#a b d
#a c d
#b c d
if (a+b>c) and (a+c>b) and (b+c>a):
    print('TRIANGLE')
elif (a+b>d) and (a+d>b) and (b+d>a):
    print('TRIANGLE')
elif (a+c>d) and (a+d>c) and (c+d>a):
    print('TRIANGLE')
elif (b+c>d) and (b+d>c) and (c+d>b):
    print('TRIANGLE')
elif (a+b==c) or (a+c==b) or (b+c==a):
    print('SEGMENT')
elif (a+b==d) or (a+d==b) or (b+d==a):
    print('SEGMENT')
elif (a+c==d) or (a+d==c) or (c+d==a):
    print('SEGMENT')
elif (b+c==d) or (b+d==c) or (c+d==b):
    print('SEGMENT')
else:
    print('IMPOSSIBLE')