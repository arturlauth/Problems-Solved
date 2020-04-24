def find_prime_factor(num):
    i = 2
    prime_factors = []
    while i in range(2, num):
        if num == 1:
            break
        elif num % i == 0:
            prime_factors.append(i)
            num = num / i
            i = 2
            num = int(num)
        else:
            i += 1
    prime_factors.append(i)
    return max(prime_factors) # remove max to return list w; all prime factor

if __name__ == '__main__':
    print(find_prime_factor(600851475143))
