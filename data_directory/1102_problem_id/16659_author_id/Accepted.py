def func(eiei):
    for i in range(0,len(eiei)):
        k=eiei[i].lower()
        Show=""
        if k!='a' and k!='e' and k!='i' \
        and k!='o'and k!='u' and k!='y':
            print('.%c'%k,end="")    
        
A=input()
func(A)
#print("eeiei")