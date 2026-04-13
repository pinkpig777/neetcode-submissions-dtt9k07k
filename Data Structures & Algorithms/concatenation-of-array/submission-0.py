class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        n = len(nums) * 2
        while i < n:
            ans.append(nums[(i)%len(nums)])
            i += 1
        return ans
