class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
            if freq[n] > majority:
                return n