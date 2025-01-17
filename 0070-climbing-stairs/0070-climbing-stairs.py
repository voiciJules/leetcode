class Solution:
    def climbStairs(self, n: int) -> int:
        # I just found a regulation for this problem. 
        # input 1 => output 1
        # input 2 => output 2
        # input 3 => output 3
        # input 4 => output 5
        # input 5 => output 8
        # input 6 => output 13
        # input 7 => output 21
        # for example, 
        # for input 3, 
        # all way to make 3 is,
        # (the ways making input 1) + 2 and (the ways making input 2) + 1
        # the code will be below.
        
        l = []
        a, b = 1, 2
        l.append(a)
        l.append(b)
        
        while len(l) <= 45:
            l.append(l[-1] + l[-2])
        
        return l[n-1]