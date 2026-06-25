class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydict = dict()


        for i in range(len(nums)):
            
            difference = target - nums[i]

            if nums[i] in mydict:
                return [mydict[nums[i]],i]

            else:
                mydict[difference] = i