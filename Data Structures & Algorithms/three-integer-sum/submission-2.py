class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 1. Sort the array
        nums.sort()
        
        # 2. Iterate + Two Pointers
        output = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i -1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0: # larger
                    right -= 1
                elif sum < 0: # smaller
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return output