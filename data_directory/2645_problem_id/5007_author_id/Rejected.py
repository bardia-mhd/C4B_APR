n = int(input())
final = int(input())
a = []
a.append([0,1,2])
a.append([1,0,2])
a.append([1,2.0])
a.append([2,1,0])
a.append([2,0,1])
a.append([0,2,1])
n %= 6
print(a[n][final])