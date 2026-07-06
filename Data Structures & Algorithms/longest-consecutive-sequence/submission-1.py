class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Loop through the entire list and form a hashmap with all values 1
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] = 1

        # 2. Loop through and find all the starting values
        longest = 0
        for key in hashmap:
            if (key-1) not in hashmap:
                max = 1
                curr = key
                while (curr+1) in hashmap:
                    max += 1
                    curr += 1
                 
                if max > longest:
                    longest = max
        
        return longest