class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        try:
            return nums.index(target)
        except ValueError:
            for i in range(len(nums)):
                if target < nums[i]:
                    return i
        return len(nums)

        # Another answer with "target in nums"
        # if target in nums:
        #     return nums.index(target)
        # else:
        #     for i in range(len(nums)):
        #         if target < nums[i]:
        #             return i
        # return len(nums)

    # At the first time, I tried to code with "if nums.index(target) != ValueError"
    # I learned that, when you need to handle errors, you can use the try-except statement.