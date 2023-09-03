def main():
    from itertools import product
    def f(a):
        x = int((a * 2. + .25) ** .5 + .51)
        if x * (x - 1) != a * 2:
            raise ValueError
        return x

    a00, a01, a10, a11 = map(int, input().split())
    try:
        for b, w in product([f(a00)] if a00 else [1, 0], [f(a11)] if a11 else [1, 0]):
            if b * w == a01 + a10:
                break
        else:
            raise ValueError
    except ValueError:
        print("Impossible")
    else:
        if w:
            a01, rest = divmod(a01, w)
            if rest:
                l = ['0' * a01, '1' * (w - rest), '0', '1' * rest, '0' * (b - a01 - 1)]
            else:
                l = ['0' * a01, '1' * w, '0' * (b - a01)]
        else:
            l = ['0' * b]
        print(''.join(l))


if __name__ == '__main__':
    main()