lucyDivision=int(input())
luckyNumber=[4,7,44,47,74,77,444,447,474,477,744,747,774,777]

# while i< len(luckyNumber):
#   if 
def compare(inputArray, compareArray):
  i=0
  while i< len(compareArray):
    if inputArray%int(compareArray[i])==0:
      return print('YES')
    else:
      i+=1
    if i==(len(compareArray)-1) and inputArray%int(compareArray[i])!=0:
      return print('NO')
      
compare(lucyDivision, luckyNumber)