Min = int(10**10)
n = input()

def next(x, a, f, s):
    global Min
    global n
    #print(Min)
    #print(n)
    if len(x) > 0:
        if a == '' or int(a) >= int(n[0:len(a)]):
            #try:
                #print(a + " " + n[0:len(a)])
            #except:
                #print("EMPTY")
            if f + 1 <= len(n) / 2:
                next(x[1:],a+'4', f+1, s)
            if s + 1 <= len(n) / 2:
                next(x[1:],a+'7', f, s+1)
    else:
        if a == '' or int(a) >= int(n[0:len(a)]):
            if int(a) < Min:
                Min = int(a)

if len(n)%2 == 1:
    n = '1'+n
elif int(n) > int('7'*int(len(n)/2)+'4'*int(len(n)/2)):
    n = '11'+n
next(n,'',0,0)
print(Min)