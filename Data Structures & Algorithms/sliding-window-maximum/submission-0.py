class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Keep track of largest values passed through
        largest = deque() # monotonic deque
        result = []

        for i, num in enumerate(nums):
            # 1. Check if the top number is out of the current window
            if largest and largest[0] < i - k + 1:
                largest.popleft()

            # 2. remove any number smaller than current number and add to queue if none
            while largest and nums[largest[-1]] < num:
                largest.pop() # pop the last
            
            largest.append(i)

            # 3. check if the first window has finished
            if i >= k - 1:
                result.append(nums[largest[0]])
        
        return result