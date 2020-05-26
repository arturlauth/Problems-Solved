def singleNumber(nums):
    ''''

        Example 1:
        Input: [2,2,1]
        Output: 1

        Example 2:

        Input: [4,1,2,1,2]
        Output: 4

    '''
    dict = {}

    for i in nums:
        dict[i] = dict.get(i, 0) + 1
    print(dict)
    for count, values in dict.items():
        if values == 1:
            return count

if __name__ == '__main__':
    list = [5, 5, 5, 10, 10, 10, 3, 4, 4, 4]
    print(singleNumber(list))