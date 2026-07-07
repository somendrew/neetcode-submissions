class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        sp = dict()

        for i in range(len(nums)):

            if nums[i] in sp:
                sp[nums[i]] += 1
            else:
                sp[nums[i]] = 1
        
        
        return sorted(sp, key=sp.get, reverse=True)[:k]



            
