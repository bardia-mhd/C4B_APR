iniStr = input()

strLen = len(iniStr)

ans=str()
index = 0
while index<strLen :
	theLower = iniStr[index].lower()
	if theLower=='a' or theLower=='e' or theLower=='i' or theLower=='o' or theLower=='u' :
		index = index+1
		continue
	else :
		ans = ans +'.'+theLower
		index = index+1

	
print(ans)