print(next(a for a in range(int(input()),12345) if len(set(str(a))) == len(str(a))))