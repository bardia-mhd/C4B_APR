if __name__ == "__main__":
    line = input()
    line = list(line.split(" "))
    a = int(line[0])
    b = int(line[1])
    n = int(line[2])
    x = 0
    if(a == 0) and (b == 0):
            print("5")
    elif(a == 0):
        print("No solution")
    elif((n % 2 == 0) and (b/a < 0)):
        print("No solution")
    elif(b/a<0):
        x = -(abs((b/a))**(1/n))
        if(x - round(x) != 0):
            print("No solution")
        else:
            print(round(x))
    else:
        x = (b/a)**(1/n)
        if(x - round(x) != 0):
            print("No solution")
        else:
            print(round(x))