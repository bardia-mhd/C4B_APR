n=input()
if(n=="a8" or n=="a1" or n=="h8" or n=="h1"):
    print(3)
elif((n[0]=='a' and n[1]!=1 and n[1]!=8) or (n[0]=='h' and n[1]!=1 and n[1]!=8) or (n[1]=='1' and n[0]!='a' and n[0]!='h') or (n[1]=='8' and n[0]!='a' and n[0]!='h')):
    print(5)
else:
    print(8)