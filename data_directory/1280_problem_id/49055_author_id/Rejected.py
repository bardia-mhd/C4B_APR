from sys import stdin
def quick(lista):
    if len(lista)<=1:
        return lista
    else:
        return quick([x for x in lista[1:] if x>lista[0]])+[lista[0]]+quick([x for x in lista[1:] if x<=lista[0]])

def main():
    n=int(stdin.readline().strip())
    lista=[int(x) for x in stdin.readline().strip().split(" ")]
    lista=quick(lista)
    suma=0
    if n==0:
        print(0)
    else:
        for i in range(len(lista)):
            suma+=lista[i]
            if suma>=n:
                print(i+1)
                break

main()