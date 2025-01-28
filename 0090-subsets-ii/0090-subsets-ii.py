class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path, k) :
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i+1, path, k)
                path.pop()

        for i in range(len(nums)+1):
            backtrack(0, [], i)

        
        output1 = set(map(tuple, result))
        output2 =[]
        for i in output1:
            if list(sorted(i)) not in output2:
                output2.append(list(sorted(i)))
        # output2 = list(map(list, output1))
        print(output2)
        return output2
