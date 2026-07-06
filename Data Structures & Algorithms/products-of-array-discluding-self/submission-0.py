class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 1. Loop through list forward
        forward = [0] * len(nums)
        res1 = 1
        for i in range(len(nums)):
            forward[i] = res1
            res1 *= nums[i]

        # 2. Loop through list backward
        backward = [0] * len(nums)
        res2 = 1
        for i in range(len(nums) - 1, -1, -1):
            backward[i] = res2
            res2 *= nums[i]

        # 3. Form the final result
        result = []
        for i in range(len(nums)):
            result.append(forward[i] * backward[i])

        return result
        