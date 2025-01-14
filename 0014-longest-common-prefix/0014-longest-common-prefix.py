class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # common_prefix = ""
        # first_str = strs[0]
        # for i in range(len(first_str)):
        #     for j in range(1, len(strs)):
        #         if first_str[i] != strs[j][i]:
        #             return common_prefix
                
        #     common_prefix += first_str[i]
        # return common_prefix

        # I ran the above code and i got an error for strs = ['ab', 'a'] because the 'a' is shorter than 'ab'. so when it pass the code if first_str[i] != strs[j][i], it makes error. So, I will find the shortest word in the list and run it with the same code.  
        common_prefix = ""
        shortest_string = min(strs, key=len)
        for i in range(len(shortest_string)):
            for j in range(len(strs)):
                if shortest_string[i] != strs[j][i]:
                    return common_prefix
                
            common_prefix += shortest_string[i]
        return common_prefix

