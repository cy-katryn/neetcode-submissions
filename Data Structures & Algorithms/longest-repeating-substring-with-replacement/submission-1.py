class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        l = 0
        maxf = 0
        longest = 0

        # Special Case: ABAABBBB, k = 1
        for r in range (len(s)):
            count[s[r]] += 1 # add to hashmap
            maxf = max(maxf, count[s[r]]) # update the most frequent letter

            # Check whether the current window
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1 # minimize the window size
            
            longest = max(longest, r - l + 1)
        
        return longest