class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        ans = []
        while heap:
            ans.append(heapq.heappop(heap))

        return ans
        
