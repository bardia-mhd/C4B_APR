import sys
import math

n, m = [int(x) for x in (sys.stdin.readline()).split()]
ss = m  % int(((1 + n) * n) / 2)

if(ss == 0):
    print(0)
    exit()
    
d = int(math.sqrt(1 + (ss * 2) * 4))

print(d)
print(ss)
sq = 0
if(int((1 + d) / 2) != 1):
    sq = int((1 + d) / 2 - 1)
else:
    sq = 1

result = int(ss - ((sq + 1) * sq / 2))

print(result)