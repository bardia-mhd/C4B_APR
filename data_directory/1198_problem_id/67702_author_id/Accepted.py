s=input()
h=0
for i in range(0,len(s)):
       if s[i] is 'H' or s[i] is 'Q' or s[i] is '9' :
           print('YES')
           h=1
           break
if h is 0:
    print("NO")