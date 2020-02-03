def td(array_nums):
    numset = set(array_nums)
    return len(array_nums) != len(numset)
print(td([1,2,3,4,5]))
print(td([1,2,3,4,4]))
print(td([1,1,2,2,3,3,4,4,5]))

