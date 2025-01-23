class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # min_index = nums.index(min(nums))
        
        # if target <= nums[-1]:
        #     for i in range(min_index, len(nums)):
        #         if nums[i] == target:
        #             return True
        # else:
        #     for i in range(min_index):
        #         if nums[i] == target:
        #             return True
        
        # return False

        if target in nums:
            return True
        return False