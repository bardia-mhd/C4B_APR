def lucky(a):
	if(a==0):
		return 0
	while(a>0):
		k=a%10
		if(k!=4 and k!=7):
			return 0
		a=a//10
	return 1

n=int(input())
c=0
while(n>0):
	k=n%10
	if(k==4 or k==7):
		c+=1
	n=n//10
if(lucky(c)==1):
	print("YES")
else:
	print("NO")