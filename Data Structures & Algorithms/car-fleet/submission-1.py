class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Solve the required time
        time = {}
        for i in range(len(position)):
            time[position[i]] = (target - position[i])/ speed[i]

        # 2. Sort the list in accordance to key in descending order (closest first)
        time = sorted(time.items(), reverse = True)

        # 3. Perform check until 
        answer = 0
        prev = None

        for post, t in time:
            if not prev or t > prev:
                answer += 1
                prev = t
        
        return answer