class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        
        s2 = str(int(s) + 1)

        output = []
        for i in s2:
            output.append(int(i))

        return output

        