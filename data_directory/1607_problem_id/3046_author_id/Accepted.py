def ff(num):
	return (int(num) // 10 - (0 if int(str(num)[0]) <= int(str(num)[-1]) else 1) + 9) if int(num) >= 10 else int(num)

def main():
    mode="filee"
    if mode=="file":f=open("test.txt","r")
    #f.readline()
    #input()
    get = lambda :[int(x) for x in (f.readline() if mode=="file" else input()).split()]
    [l,r]=get()
    print(ff(r) - ff(l-1))
    


    if mode=="file":f.close()


if __name__=="__main__":
    main()