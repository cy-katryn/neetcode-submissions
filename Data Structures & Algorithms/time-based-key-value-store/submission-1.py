class TimeMap:

    def __init__(self):
        """Initialize a list"""
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        """O(1) operation, to simple add element into list"""
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        """Binary search if direct lookup failed"""

        # 1. Direct look up first
        values = self.store.get(key, [])

        if not values: # no values stored for this key
            return ""

        # 2. Perform binary search
        left = 0 
        right = len(values) - 1
        answer = ""
        
        while left <= right:
            mid = left + (right - left) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
                answer = values[mid][0]
            else:
                right = mid - 1
        
        return answer