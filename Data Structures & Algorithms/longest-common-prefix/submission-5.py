class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        #lets say first string is the shortest
        #"dance" =  range 5 : (0,1,2,3,4)
        for i in range(len(strs[0])):

            #range 3 : ["dag","danger","damage"]
            for s in strs[1:]:
                # LOGIC 1: if any string is shorter than current index OR characters mismatch,
                #LOGIC 2: search for "d" in dance not equal to "d" in ["dag","danger","damage"]
                if i == len(s) or strs[0][i] != s[i]:
    
                    return strs[0][:i]
        
        #if loop completes, entire first string is common prefix
        return strs[0]
 
                





        