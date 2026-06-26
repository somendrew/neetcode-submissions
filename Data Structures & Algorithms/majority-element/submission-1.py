class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dit = dict()

        for i in range(len(nums)):
            if nums[i] not in dit:
                dit[nums[i]] = 1

            else:
                dit[nums[i]] += 1

        max_key = max(dit, key=dit.get)
        return max_key