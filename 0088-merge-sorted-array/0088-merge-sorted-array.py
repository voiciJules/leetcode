class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mem_j = 0
        print(m)
        for i in range(m+n):
            for j in range(mem_j, n):
                if nums1[i] >= nums2[j]:
                    nums1.insert(i, nums2[j])
                    mem_j = j+1  
                    print("if",i, j, mem_j, nums1, nums2)
                    break                
                else:
                    print("else", i, j, mem_j, nums1, nums2)
                    break
            print(i, mem_j, nums1)
        
        for i in range(n):
            nums1.pop()
        
        nums1.extend(nums2[mem_j:])
            

            