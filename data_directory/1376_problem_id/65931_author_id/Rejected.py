import sys

def work(mid, n, k):
    v = mid;
    total = 0;
    while(v != 0):
        total += v;
        v = int(v/k);
        if(mid == 53):
            print("v: " + str(v));
    if(total < n):
         return False;
    return True;

line = input().split(" ");

n = int(line[0]);
k = int(line[1]);

lo = 1;
hi = n;

mid = int((lo+hi)/2);

while(mid != hi):
    if(work(mid, n, k)):
        hi = mid;
    else:
        lo = mid;
    mid = int((lo+hi)/2 + .5);
    
sys.stdout.write(str(mid));