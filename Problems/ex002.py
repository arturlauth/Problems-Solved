def fibonacci_sequence(max):
    sequence = []
    x = 1
    next = 2

    while x <= max:
        sequence.append(x)
        sequence.append(next)
        x += next
        next += x
    return sequence

def sum_even(list):
    sum = 0

    for num in list:
        if num % 2 == 0:
            sum += num
    return sum

if __name__ == '__main__':
    print(sum_even(fibonacci_sequence(4E6)))