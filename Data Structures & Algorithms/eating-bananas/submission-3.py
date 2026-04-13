class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(piles, h, k):
            k_cnt = 0
            for p in piles:
                k_cnt += (p + k - 1) // k
            return k_cnt <= h
        l, r = 1, max(piles)

        while l < r:
            k = (l + r) // 2
            if isValid(piles, h, k):
                r = k
            else:
                l = k + 1
        return l 
