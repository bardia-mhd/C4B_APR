mat = [list(map(int, input().split())) for i in range(4)]

p1 = sum([mat[0][1], mat[0][2], mat[0][0], mat[1][0], mat[2][1], mat[3][2]])
p2 = sum([mat[0][2], mat[1][0], mat[1][2], mat[1][1], mat[2][0], mat[3][1]])
p3 = sum([mat[0][1], mat[1][2], mat[2][0], mat[2][1], mat[2][2], mat[3][0]])
p4 = sum([mat[0][0], mat[1][1], mat[2][2], mat[3][0], mat[3][1], mat[3][2]])

if mat[0][3] == 1 and p1 >= 1:
    print('YES')
elif mat[1][3] == 1 and p2 >= 1:
    print('YES')
elif mat[2][3] == 1 and p3 >= 1:
    print('YES')
elif mat[3][3] == 1 and p4 >= 1:
    print('YES')
else:
    print('NO')