class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 1. Loop through the string t to form a hashmap
        count_t = defaultdict(int)
        for letter in t:
            count_t[letter] += 1
        
        count_s = defaultdict(int) # another to keep track if current windows is valid
        
        l = 0
        minL = math.inf
        minW = [-1, -1]
        need = len(count_t) # count the number of unique letters the window must have
        have = 0 # count how many the current window actually fulfilled

        # 2. Loop through the string s with sliding window
        for r in range(len(s)):

            if s[r] in count_t:
                count_s[s[r]] += 1
            
                if count_s[s[r]] == count_t[s[r]]:
                    have += 1

            while need == have and l <= r:
                if (r - l + 1) < minL:
                    minL = r - l + 1
                    minW = [l, r]

                if s[l] in count_t:
                    if count_s[s[l]] == count_t[s[l]]:
                        have -= 1
                    count_s[s[l]] -= 1

                l += 1
                        
        return s[minW[0] : minW[1] + 1] if minL != math.inf else ""