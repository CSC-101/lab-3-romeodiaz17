def tally(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total += num
    return total           # num = 4 total = 4,  num = 9 total = 13,  num = 2 total = 15,  num = 1 total = 16

result = tally([4, 9, 2, 1])

def copy(nums : list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
    return new_list     # idx = 0 newlist = [4],idx = 1 newlist = [4,9],idx = 2
    # newlist = [4,9,2] idx = 3 newlist = [4,9,2, 1]

result1= copy([4, 9, 2, 1])   # this code makes a new list and dosent change original


def increment_all(nums : list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)
    return new_list     # value = 4 , newlist = [5],value = 9 , newlist = [5,10]
#value = 2 , newlist = [5,10,3],value = 1 , newlist = [5,10,3,2]

result3= increment_all([4, 9, 2, 1])
