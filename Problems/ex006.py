def solve():
    sum = 0
    sum_2 = 0
    for i in range(1,101):
        sum = i**2 + sum
        sum_2 += i
    sum_2_square = sum_2**2

    return sum_2_square - sum

if __name__ == '__main__':
    print(solve())