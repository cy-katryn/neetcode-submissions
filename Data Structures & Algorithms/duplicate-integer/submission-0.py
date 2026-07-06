class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create hashmap
        hashmap = {}

        # Loop through the array once to and mark true for the key
        for num in nums:
            if num in hashmap:
                return True
            hashmap[num] = True
        
        return False