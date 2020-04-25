def largest_palindrome_number():
    palindrome_numbers = []
    for i in range(100,999):
        for j in range(100,999):
            number = i*j
            number_str = str(number)
            digit_list = list(map(int, number_str))
            inverted_number = []
            for digit in digit_list:
                inverted_number.insert(0, digit)

            if digit_list == inverted_number:
                palindrome_numbers.append(number)
    return max(palindrome_numbers)

if __name__ == '__main__':
    print(largest_palindrome_number())