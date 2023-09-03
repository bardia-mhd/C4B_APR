if __name__ == "__main__":
    N = int(input())
    S = input().split(":")
    H = S[0]
    M = S[1]
    res = 114514
    ans = ""
    if N == 12:
        for i in range(0, 13):
            for j in range(0, 60):

                h = str(i)
                m = str(j)
                while (len(h) != 2):
                    h = "0" + h
                while (len(m) != 2):
                    m = "0" + m

                diff = 0
                for x,y in zip(h, H):
                    if (x != y):
                        diff += 1

                for x,y in zip(m, M):
                    if (x != y):
                        diff += 1

                if (diff < res):
                    res = diff
                    ans = h + ":" + m
    else:
        for i in range(1, 24):
            for j in range(0, 60):
                h = str(i)
                m = str(j)
                while (len(h) != 2):
                    h = "0" + h
                while (len(m) != 2):
                    m = "0" + m

                diff = 0
                for x,y in zip(h, H):
                    if (x != y):
                        diff += 1

                for x,y in zip(m, M):
                    if (x != y):
                        diff += 1
                if (diff < res):
                    res = diff
                    ans = h + ":" + m
    print (ans)