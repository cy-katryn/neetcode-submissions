class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)

        length = 0 # store max length found
        l = 0
        maxf = 0 # tracks the frequency of the most common char

        for r in range(len(s)):
            hashmap[s[r]] += 1

            maxf = max(maxf, hashmap[s[r]])

            if (r - l + 1) - maxf > k:
                hashmap[s[l]] -= 1
                l += 1

            length = max(length, r - l + 1)

        return length

            
