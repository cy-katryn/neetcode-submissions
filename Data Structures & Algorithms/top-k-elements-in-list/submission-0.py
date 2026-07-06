class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Loop through the hashmap to record unique numbers and its corresponding frequency
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
            
        # 2. Loop through the hashmap and create buckets
        k_list = [[] for _ in range(len(nums) + 1)]
        for key in hashmap:
            k_list[hashmap[key]].append(key)

        answer = []
        for i in range(len(nums), -1, -1):
            if k_list[i] != None:
                for num in k_list[i]:
                    answer.append(num)

                    if len(answer) == k:
                        return answer