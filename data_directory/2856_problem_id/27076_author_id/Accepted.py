l1,s1,r1,p1=map(int,input().split())
l2,s2,r2,p2=map(int,input().split())
l3,s3,r3,p3=map(int,input().split())
l4,s4,r4,p4=map(int,input().split())
f="NO"
if p1==1 and (s1==1 or l1==1 or r1==1 or r4==1 or l2==1 or s3==1): f="YES"
if p2==1 and (s2==1 or l2==1 or r2==1 or r1==1 or l3==1 or s4==1): f="YES"
if p3==1 and (s3==1 or l3==1 or r3==1 or r2==1 or l4==1 or s1==1): f="YES"
if p4==1 and (s4==1 or l4==1 or r4==1 or r3==1 or l1==1 or s2==1): f="YES"
print(f)