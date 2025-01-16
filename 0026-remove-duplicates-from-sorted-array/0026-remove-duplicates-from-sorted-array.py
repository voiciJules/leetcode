class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        index = 1
        for i in range(1,length):
            if nums[i-1] != nums[i]:
                nums[index] = nums[i]
                index += 1        
        return index
            
    # This question is a bit ambiguous. After reading a solution, I understood the question and what to do exactly, but now with the question of the editor. 
