year=int(input())
lis=[str(x) for x in str(year)]
beau=0

for i in range(year+1,10000):
	temLis=[]
	temLis=[str(x) for x in str(i)]
	tem_set=set(temLis)
	if len(tem_set)==4:
		beau=i
		break
print(i)