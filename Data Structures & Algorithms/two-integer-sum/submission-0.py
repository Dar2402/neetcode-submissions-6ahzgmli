class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] + nums[j] == target:
        #             res.append(i)
        #             res.append(j)
        #             break

        
        chk = {}

        """
        {
            4: 0,
            5: 1,
        }
        [4, 5, 6]
        4-> diff = 6
        5-> diff = 5
        6-> diff = 4
        """

        for i in range(n):
            diff = target - nums[i]
            
            if diff in chk:
                return [chk[diff], i]
            
            chk[nums[i]] = i


        return res
        