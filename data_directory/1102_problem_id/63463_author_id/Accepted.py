word = input()
word = word.lower()
emp=''
for i in word : 
	if( i=='a' or i=='o' or i=='y' or i=='e' or i=='u' or i=='i') : 
		pass
	else : 
		emp=emp+'.'+i
print (emp)