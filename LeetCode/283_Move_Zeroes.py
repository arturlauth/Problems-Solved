def moveZeroes(nums):

    for i in range(nums.count(0)):
        nums.remove(0)
        nums.append(0)
    return None


if __name__ == '__main__':
    nums = [0,1,0,3,4,5,0,12,3,0,0,0,0,0,12,12]
    moveZeroes(nums)
    print(nums)