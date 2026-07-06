class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        longest = 0
        start = 0
        end = 0

        for i in range(len(s)):
            if s[i] in hashmap:
                start = max(start, hashmap[s[i]] + 1)
            
            longest = max(longest, i - start + 1)
            hashmap[s[i]] = i

        return longest