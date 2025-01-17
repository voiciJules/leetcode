class Solution:
    def mySqrt(self, x: int) -> int:
        # this is the way to use built-in function of math
        # return(math.floor(math.sqrt(x)))

        #Binary search
        if x == 0:
            return 0
        elif x == 1:
            return 1
        
        start, end, mid  = 1, x, int((1+x)/2)
        print(start, end, mid)
        while start != mid:
            mid = int((start + end) / 2)
            print(start, end, mid)
            if x == (mid ** 2):
                return mid
            elif x < (mid ** 2):
                end = mid
            else: 
                start = mid
        
        return start
        


        



