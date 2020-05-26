def solve():

    for a in range(1, 1001):
        for b in range(1, 1001):
            c = 1000 - a - b
            if a+b+c == 1000:
                if a < b and b < c and a**2 + b**2 == c**2:
                    return a*b*c


if __name__ == '__main__':
    print(solve())
