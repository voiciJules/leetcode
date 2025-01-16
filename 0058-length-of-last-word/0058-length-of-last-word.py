class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reversed_s = s[::-1].strip()
        try:
            return reversed_s.index(" ")
        except ValueError:
            return len(reversed_s)


        # After reversing the string and removing leading and trailing whitespaces of the string 's', return the index of the first ' '. 

