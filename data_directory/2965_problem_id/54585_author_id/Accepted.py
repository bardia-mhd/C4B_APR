DIRS = ['v', '<', '^', '>']

a, b = map(DIRS.index, input().split())
n = int(input())

delta = (b - a + 4) % 4

if delta == 0 or delta == 2:
    print('undefined')
elif delta == n % 4:
    print('cw')
else:
    print('ccw')
  
1