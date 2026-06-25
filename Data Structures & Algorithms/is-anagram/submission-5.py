class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        heap = dict()

        for i in range(len(s)):
            
            if s[i] not in heap:
                heap[s[i]] = 1
            else:
                heap[s[i]]+=1

        
        for i in range(len(t)):

            if t[i] not in heap:
                heap[t[i]] = 1

            elif t[i] in heap:
                heap[t[i]] -=1

        if any(heap.values()) !=0:
            return False
        else:
            return True
            
        
        

        

            
        



        