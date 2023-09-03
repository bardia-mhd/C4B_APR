from math import hypot

def d_sq(a, b):
    return hypot(a[0] - b[0], a[1] - b[1])


def right_tri(a, b, c):
    sides = sorted([d_sq(a, b), d_sq(b, c), d_sq(c, a)])
    return 2 * sides[-1] == sum(sides)

off_sets = [
    [0, -1],
    [0, 1],
    [-1, 0],
    [1, 0],
]

points = list(zip(*(iter(map(int, input().split())),) * 2))

if right_tri(*points):
    print("RIGHT")
else:
    almost_right = False
    for i in range(3):
        for off_set in off_sets:
            points[i] = (points[i][0] + off_set[0], points[i][1] + off_set[1])
            if right_tri(*points) and len(set(points)) == 3:
                almost_right = True
            points[i] = (points[i][0] - off_set[0], points[i][1] - off_set[1])
    if almost_right:
        print("ALMOST")
    else:
        print("NEITHER")