def mul_of_3_5(lenght):
    list = range(lenght)
    soma = 0
    for num in list:
        if num % 3 == 0 or num % 5 == 0:
            soma += num
    return soma

if __name__ == '__main__':
    print(mul_of_3_5(1000))
