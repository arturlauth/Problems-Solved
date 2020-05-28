def dictCounter(nums):

    dict = {}
    for x in nums:
        if dict.get(x) is None:
            dict[x] = 1
        else:
            dict[x] = dict.get(x) + 1

    return majorityElement(dict)

def majorityElement(dict):

    list_value = list(dict.values())
    index_major = list_value.index(max(list_value))
    list_keys = list(dict.keys())
    major_element = list_keys[index_major]

    return major_element


if __name__ == '__main__':
    print(dictCounter([3,2,1,1,1,1,1,3,3,3,3,3,3,3,3,3,1,1,4,4,4,4,4,3,5,5]))