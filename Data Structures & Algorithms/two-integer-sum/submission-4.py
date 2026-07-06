class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 1. Loop through the array and form hashmap
        hash = {}
        for i, num in enumerate(nums):
            if num not in hash:
                hash[num] = []
            hash[num].append(i)
        
        # 2. Loop through entire array and find if corresponding complement is available
        for key in hash:
            complement = target - key
            if complement in hash:
                if complement == key:
                    if len(hash[key]) >= 2:
                        return [hash.get(key)[0], hash.get(key)[1]]
                else:
                    return [hash.get(key)[0], hash.get(complement)[0]]

        return [None, None]