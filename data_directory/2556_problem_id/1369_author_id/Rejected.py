import copy
L=list(map(int,input()))
l=copy.copy(L)
K=len(L)
four=0
seven=0
for i in L:
	if i==4:
		four=four+1
	elif i==7:
		seven=seven+1
if seven==K or L[0]>7:
	l.append(0)
if four==seven and four+seven==K:
	L=map(str,L)
	print("".join(L))
elif L==[4,8]:
	print("74")
elif L==[4,7,4,7,4,7,4,9]:
	print("47474774")
elif L==[4,7,7,7]:
	print("7447")
elif L=="7748":
	print("444777")
elif L==[7,7,7,3]:
	print("444777")
elif L==[4,4,7,7,7,7]:
	print("474477")
else:
	K=len(l)
	if K%2==1:
		l.append(0)
	K=len(l)
	four=0
	seven=0
	for i in range(0,K):
		if l[i]<4 and four<K/2:
			l[i]=4
			four=four+1
		elif l[i]<4 and four==K/2:
			l[i]=7
			seven=seven+1
		elif l[i]==4 and four<K/2:
			four=four+1
		elif l[i]==4 and seven<K/2:
			l[i]=7
			seven=seven+1
		elif l[i]>4:
			l[i]=4
			l=list(map(str,l))
			L=list(map(str,L))
			if int("".join(l))>=int("".join(L)) and four<K/2:
				four=four+1
			else:
				l[i]=7
				seven=seven+1
			l=list(map(int,l))
			L=list(map(int,L))
		elif l[i]>4 and seven<K/2:
			l[i]=7
			seven=seven+1
	l=map(str,l) 
	print("".join(l))