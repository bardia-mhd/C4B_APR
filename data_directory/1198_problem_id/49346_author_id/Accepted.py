x = input()
a=list()
for i in range(0,len(x)):
	a.append(x[i])
if ('H'==x[0]) or ('Q'==x[0]) or ('9'==x[0]) or ('H' in a) or ('Q' in a) or ('9' in a):
	print("YES")
else:
	print("NO")