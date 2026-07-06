class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        answer = 0

        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            answer = max(answer, area)
            print(f"{heights[left]}, {heights[right]}, {answer}")

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] <= heights[right]:
                left += 1
            
        return answer