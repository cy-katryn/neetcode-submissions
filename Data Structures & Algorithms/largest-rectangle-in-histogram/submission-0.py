class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                pop_height, pop_ind = stack.pop()

                # area of popped bar
                width = i - pop_ind
                max_area = max(max_area, width * pop_height)

                start = pop_ind
            
            stack.append((height, start))
        
        # clean up whatever is left of stack
        for pop_height, pop_ind in stack:
            width = len(heights) - pop_ind
            max_area = max(max_area, width * pop_height)
        
        return max_area