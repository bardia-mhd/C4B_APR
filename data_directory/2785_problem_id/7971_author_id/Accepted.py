n=input()
m=n.count("VK")
n=n.replace("VK", "O")
if "VV" in n or "KK" in n:
   m=m+1
print(m)