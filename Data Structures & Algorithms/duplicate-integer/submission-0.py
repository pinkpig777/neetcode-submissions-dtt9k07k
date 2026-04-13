class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = defaultdict(int)
        for n in nums:
            if freq[n] == 1:
                return True
            else:
                freq[n] += 1
        return False