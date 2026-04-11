class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # return any(
        #     nums.count(i) for i in nums
        #     if nums.count(i) > 1
        # )

        return True if len(set(nums)) != len(nums) else False
        