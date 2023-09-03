from sys import stdin

def transpuesta(matriz):
    trans= []
    for j in range(len(matriz)):
        columna= []
        for i in range(len(matriz)):
            columna.append(matriz[i][j])
        trans.append(columna)
    return trans
    

def main():
    n= [ int(x) for x in stdin.readline().split()]
    matriz= []
    while n:
        matriz.append(n)
        n= [ int(x) for x in stdin.readline().split()]
    trans= transpuesta(matriz)
    col = trans.index(max(trans))+1
    fil = matriz.index(max(matriz))+1
    if col< 3 and fil < 3:
        col-=3
        fil-=3
        print(abs(col)+abs(fil))
    elif col>3 and fil>3:
        col-=3
        fil-=3
        print(col+fil)
    elif col> 3 and fil<3:
        col-=3
        fil-=3
        print(col+abs(fil))
    else:
        col-=3
        fil-=3
        print(fil+abs(col))
    
    
main()