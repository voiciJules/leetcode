class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        output = 0
        
        for i in range(len(nums)):
            if dic.get(nums[i]) == 2:
                nums[i] = ('_')
            else:
                if dic.get(nums[i]) == None:
                    dic[nums[i]] = 0
                dic[nums[i]] += 1
                output += 1
        for val in nums:
            if val == "_":
                nums.remove("_")
                nums.append("_")

        return output

        # How to use dictionary
        # when dict.get('key') has no result => return None
        # when dict['key] has no result => Key Error
        # At the first time to add some key and value, you have to dict[key] = value