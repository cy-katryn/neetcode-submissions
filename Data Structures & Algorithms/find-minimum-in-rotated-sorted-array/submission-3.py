class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1. Assume nums[0] to be ans
        ans = nums[0]

        left = 0
        right = len(nums) - 1

        # 2. While loop if current subarray isn't ascending
        while left < right:
            mid = left + (right - left) // 2

            # if nums[mid] is smaller then we get the first half
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
            
        return nums[left]