class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l <= r:
            mid = l + (r-l) // 2 
            hr_cnt = 0
            for pile in piles:
                hr_cnt += (pile + mid - 1) // mid  # 向上取整
            if hr_cnt > h:
                l = mid + 1
            else:
                r = mid - 1
        return l