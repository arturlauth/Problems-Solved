def solve(posicao_primo):
    num = 2
    counter = 0
    while True:
        counter2 = 0
        for i in range(1, num+1):
            if num % i == 0 and counter2 <= 2:
                counter2 += 1
        if counter2 == 2:
            counter += 1

        if counter < posicao_primo:
            num += 1
        else:
            break
        print(counter)
    return num

if __name__ == '__main__':
    print(solve(10001))