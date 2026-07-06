class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hashmap = defaultdict(int)
        for num in nums:
            if num not in hashmap:

                # 1. get the adjacent length
                left = hashmap.get(num-1, 0)
                right = hashmap.get(num+1, 0)

                # 2. total length
                length = left + right + 1

                # 3. store length
                hashmap[num] = length
                hashmap[num - left] = length
                hashmap[num + right] = length

                longest = max(length, longest)
        
        return longest