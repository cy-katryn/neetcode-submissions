class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = [] # should store positions

        for i in range(len(temperatures)):
            # loop through stack and check if current element is larger
            while (len(stack) > 0):
                if temperatures[stack[-1]] < temperatures[i]:
                    results[stack[-1]] = i - stack[-1]
                    stack.pop()
                else:
                    break

            stack.append(i)
        
        return results