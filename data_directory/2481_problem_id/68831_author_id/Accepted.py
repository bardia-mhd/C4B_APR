import math
n = int(input())
dict = {1:'Sheldon',2:'Leonard',3:'Penny',4:'Rajesh',5:'Howard'}
if n==1: print(dict[n])
else:
    l = int(math.log2((n-1)/5+1))
    m = n - 5*(2**l-1)
    m = math.ceil(m/(2**l))
    print(dict[m])