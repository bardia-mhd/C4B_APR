def gcd(x,y):
    if x % y == 0:
        return y
    else:
        return gcd(y,x%y)
def lcm(x,y):
    return (x*y) // gcd(x,y)
t,w,b = map(int,input().split())
r = min(w,b)-1
s = (t//lcm(w,b))*lcm(w,b)
index = 0
index = min(t-s,r)

x = (t//(lcm(w,b)))*(r+1) + index 
c = gcd(x,t)
num = x // c
den = t // c
print("%d/%d" % (num,den))