def searchInsert(nums, target):
    for i in range(len(nums)):
        # print(i)
        if nums[i] == target:
            # print(i)
            return i
        if nums[i] > target:
            return i



print(searchInsert([1,2,5,7], 5))
print(searchInsert([1,2,5,7], 4))
# print(searchInsert([1,2,5,7], 5))