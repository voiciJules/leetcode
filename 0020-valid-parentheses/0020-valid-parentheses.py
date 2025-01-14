class Solution:
    def isValid(self, s: str) -> bool:
        # Opening bracket only can come first. Closing bracket can not come first. 
        # The length of input string should be even number
        # if there is one opening bracket, it should have one closing bracket corresponding to the opening bracket. 
        dic = {'(':')', '[':']', '{':'}'}
        stack = []
        if len(s) % 2 != 0:
            return False
        for i in s:
            if dic.get(i):
                stack.append(dic.get(i))
            elif len(stack) == 0:
                return False
            else:
                if stack[-1] == i:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
        