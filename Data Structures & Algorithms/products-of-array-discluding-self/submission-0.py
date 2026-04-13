class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        r = [1] * n

        prd = 1
        for i in range(n):
            if i != 0:
                j = i - 1
                prd = prd * nums[j] 
                l[i] = prd
            else:
                l[0] = 1
        
        prd = 1
        for i in range(n - 1, -1, -1):
            if i != (n - 1):
                j = i + 1
                prd = prd * nums[j]
                r[i] = prd
            else:
                r[i] = 1
                
        
        return [i * j for i, j in zip(l, r)]