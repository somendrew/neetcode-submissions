class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq_map = {}

        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            
            else:
                freq_map[num] += 1
            
        min_heap = []

        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq,num))

            if len(min_heap)> k:
                heapq.heappop(min_heap)

        return [num for freq, num in min_heap ]




            
