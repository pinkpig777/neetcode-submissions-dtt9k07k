"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.end)
        prev = -1
        for interval in intervals:
            if interval.start < prev:
                return False
            else:
                prev = interval.end
        return True
            