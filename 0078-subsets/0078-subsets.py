class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
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
            # print(i, result)

        # print(result)
        return result

       