class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        occ_counter = dict()
        
        for char in s:
            if char in occ_counter:
                occ_counter[char] +=1
            else:
                occ_counter[char] = 1
        
        for char in t:
            if char in occ_counter:
                occ_counter[char] -=1
            else:
                return False
            
        for val in occ_counter.values():
            if val != 0:
                return False
        
        return True