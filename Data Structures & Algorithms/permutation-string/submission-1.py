class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Idea: Slide a len(s1) window through s2
        left = 0    
        right = len(s1) - 1

        # 1. Form the first array with frequencies
        count_s1 = [0] * 26
        count_s2 = [0] * 26

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            count_s1[ord(s1[i]) - ord('a')] += 1 
            count_s2[ord(s2[i]) - ord('a')] += 1
    
        while right < len(s2):
            if count_s1 == count_s2:
                return True
            
            count_s2[ord(s2[left]) - ord('a')] -= 1
            
            if right + 1 < len(s2):
                count_s2[ord(s2[right + 1]) - ord('a')] += 1

            left += 1
            right += 1
        
        return False