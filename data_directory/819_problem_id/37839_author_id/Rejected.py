s=input()
p=1
l=0
for i in range(len(s)):
	if s[i]=='A' or s[i]=='O' or s[i]=='Y' or s[i]=='E' or s[i]=='U' or s[i]=='I':
		if p>l:
			l=p
		p=1
	else:
		p=p+1
print(l)