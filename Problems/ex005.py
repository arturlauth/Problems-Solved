import cProfile


def solve():
    num = 20
    remainder = 0
    divisors = list(range(1,20))

    while True:
        for i in divisors:
            remainder = num % i + remainder
            if remainder != 0:
                break

        if remainder == 0:
            return num
        else:
            num += 2
            remainder = 0

if __name__ == '__main__':
    print(cProfile.run('solve()'))