class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        # Loop through the list
        for i, num in enumerate(nums):
            # 1. Check when complement exist
            complement = target - num
            if complement in hashmap:
                return [hashmap.get(complement), i]
            
            hashmap[num] = i

        return [None, None]