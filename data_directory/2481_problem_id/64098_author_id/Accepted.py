n=input()
n=int(n)
index=0
i=0
list1=['Sheldon', 'Leonard', 'Penny', 'Rajesh', 'Howard']
while n>0:
	if index==5:
		index=0
		i+=1
	if n-(2**i)>0:
		index+=1
		n=n-(2**i)
	else:
		print(list1[index])
		break