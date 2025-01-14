class Solution:
    def romanToInt(self, s: str) -> int:

        checkList = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000, 'IV': 4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        idx = 0
        result = 0
        while idx < len(s):
            if s[idx] == 'I':
                if s[idx:idx+2] == 'IV':
                    result += checkList.get('IV')
                    idx += 2
                    continue
                elif s[idx:idx+2] == 'IX':
                    result += checkList.get('IX')
                    idx += 2
                    continue
                else:
                    result += 1
                    idx += 1
                    continue
            if s[idx] == 'X':
                if s[idx:idx+2] == 'XL':
                    result += checkList.get('XL')
                    idx += 2
                    continue
                elif s[idx:idx+2] == 'XC':
                    result += checkList.get('XC')
                    idx += 2
                    continue
                else:
                    result += 10
                    idx += 1
                    continue
            if s[idx] == 'C':
                if s[idx:idx+2] == 'CD':
                    result += checkList.get('CD')
                    idx += 2
                    continue
                elif s[idx:idx+2] == 'CM':
                    result += checkList.get('CM')
                    idx += 2
                    continue
                else:
                    result += 100
                    idx += 1
                    continue
            result += checkList.get(s[idx])
            idx += 1
        
        return result

        # The above is my answer for this question and I looked at the discussion to find a better solution. The below one is simpler and more readable. 

        # IV, IX, XL, XC... 
        # the above two caracters have a simple regulation. 
        # when the first letter's number is smaller than the second letter, 
        # the first letter's number became minus. 
        # for example, IV = I is 1 and V is 5. So I < V. 
        # Therefore, the first letter's number is -1.  
        # roman = {
        #     'I':1, 
        #     'V':5,
        #     'X':10,
        #     'L':50,
        #     'C':100,
        #     'D':500,
        #     'M':1000
        # }
        # total = 0
        # for i in range(len(s)-1):
        #     if roman[s[i]] < roman[s[i+1]]:
        #         total -= roman[s[i]]
        #     else:
        #         total += roman[s[i]]
        # return total + roman[s[-1]]




