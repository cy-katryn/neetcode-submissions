class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = 0

        while left <= right:
            print(left, right)
            mid = left + int((right - left) / 2) # calculate mid point
            print(  mid)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        
        return -1