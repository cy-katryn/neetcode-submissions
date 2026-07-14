class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 1. Find the max of the piles as 'right'
        left = 1 # constraints
        right = max(piles)
        
        # 2. Calculate midpoint then loop through the list    
        k = right
        while left <= right:
            mid = left + (right - left) // 2

            # 3. Check how many counts were actually used
            count = 0
            for pile in piles:
                count += (pile + mid - 1) // mid # round up

            if count > h: # exceeded limit
                left = mid + 1 # need a larget rate
            else: # lower than limit
                right = mid - 1
                k = min(k, mid)
        
        return k

                