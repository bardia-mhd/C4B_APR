name = input()
length = len(name)
list=set()
for letter in name:
  list.add(letter) 
print(list)
if len(list)%2 ==0:
  print("CHAT WITH HER!")  
else:
  print("IGNORE HIM!")