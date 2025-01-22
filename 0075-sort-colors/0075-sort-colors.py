class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                del nums[i]
                nums.insert(0, 0)
        
        howmany_2 = 0
        for i in range(len(nums)):
            if nums[i] == 2:
                howmany_2 += 1
        for i in range(howmany_2):
            nums.remove(2)
            nums.append(2)
    # it's about the functions : del, insert, append, remove