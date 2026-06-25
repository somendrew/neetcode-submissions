class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        case = dict()

        for num in nums:

            #if already present
            if num in case:
                return True
            
            else:
                case[num] = 1
        
        return False




