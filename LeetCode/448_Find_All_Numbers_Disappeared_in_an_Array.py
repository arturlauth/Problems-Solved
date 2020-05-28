def findDisappearedNumbers(nums):

    u_nums = set(nums)
    list_missing_numbers = []

    for x in range(1, len(nums) + 1):
        if (x in u_nums) is False:
            list_missing_numbers.append(x)

    return list_missing_numbers

if __name__ == '__main__':
    print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))