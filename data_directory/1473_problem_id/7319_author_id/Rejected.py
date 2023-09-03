def isRightAngled(x1,y1,x2,y2,x3,y3):
	if x2 == x1 or x3 == x1 or x3 == x2:
		if y2 == y1 or y3 == y1 or y3 == y2:
			if (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3):
				return False
			return True
	slope1 = (y2-y1)/(x2-x1)
	slope2 = (y3-y1)/(x3-x1)
	slope3 = (y3-y2)/(x3-x2)
	if round(slope1 * slope2,8) == -1:
		return True
	elif round(slope1 * slope3,8) == -1:
		return True
	elif round(slope2 * slope3,8) == -1:
		return True
	else:
		return False

x1,y1,x2,y2,x3,y3 = list(map(int,input().split()))

if isRightAngled(x1,y1,x2,y2,x3,y3):
	print('RIGHT')
	exit(0)

if isRightAngled(x1+1,y1,x2,y2,x3,y3) or isRightAngled(x1-1,y1,x2,y2,x3,y3) or isRightAngled(x1,y1+1,x2,y2,x3,y3) or isRightAngled(x1,y1-1,x2,y2,x3,y3) or isRightAngled(x1,y1,x2+1,y2,x3,y3) or isRightAngled(x1,y1,x2-1,y2,x3,y3) or isRightAngled(x1,y1,x2,y2+1,x3,y3) or isRightAngled(x1,y1,x2,y2-1,x3,y3) or isRightAngled(x1,y1,x2,y2,x3+1,y3) or isRightAngled(x1,y1,x2,y2,x3-1,y3) or isRightAngled(x1,y1,x2,y2,x3,y3+1) or isRightAngled(x1,y1,x2,y2,x3,y3-1):
	print('ALMOST')
	exit(0)

print('NEITHER')