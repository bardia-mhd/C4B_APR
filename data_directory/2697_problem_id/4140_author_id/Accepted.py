def mp():  return map(int,input().split())
def lt():  return list(map(int,input().split()))
def pt(x):  print(x)
def ip():  return input()
def it():  return int(input())
def sl(x):  return [t for t in x]
def spl(x): return x.split()
def aj(liste, item): liste.append(item)
def bin(x):  return "{0:b}".format(x)
def listring(l): return ' '.join([str(x) for x in l])
def ptlist(l): print(' '.join([str(x) for x in l]))


a,b = mp()
c,d = mp()

def pgcd(x,y):
    if x > y:
        return pgcd(y,x)
    if y%x == 0:
        return x
    else:
        return pgcd(y%x,x)
if (abs(b-d))%pgcd(a,c)!= 0:
    pt(-1)
else:
    k=b
    s=d
    while k != s:
        if k>s:
            s+=c
        else:
            k+=a
    pt(k)