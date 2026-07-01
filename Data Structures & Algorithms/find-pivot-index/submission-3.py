class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left_sum = 0

        total = sum(nums)

        if len(nums) <= 2 :
            return 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            else:
                left_sum+=nums[i]

        return -1
            





        