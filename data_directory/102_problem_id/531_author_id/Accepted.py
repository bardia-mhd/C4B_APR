'''input
100 33 34
'''
d1, d2, d3 = map(int, input().split())
print(min(2*d1+2*d2, d1+d2+d3, 2*d1+2*d3,2*d2+2*d3))