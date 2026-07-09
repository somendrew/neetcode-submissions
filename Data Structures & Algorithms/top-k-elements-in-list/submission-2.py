class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count how many times each number appears
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] = freq_map[num] + 1
            else:
                freq_map[num] = 1

        # Step 2: Use a min-heap of size k to keep track of the k most frequent numbers
        # heap stores tuples of (frequency, number)
        min_heap = []
        for num, freq in freq_map.items():
            heapq.heappush(min_heap, (freq, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)  # remove the least frequent element so far

        # Step 3: Extract numbers from the heap (order doesn't matter for this problem)
        return [num for freq, num in min_heap]



            
