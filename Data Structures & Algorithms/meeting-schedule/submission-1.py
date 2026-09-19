"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[int]) -> bool:
        intervals.sort(key=lambda x:x.start)

        staging = []

        for interval in intervals:
            if len(staging) < 1:
                staging.append(interval)
            else:
                if staging[-1].start > interval.end or interval.start >= staging[-1].start and interval.start < staging[-1].end:
                    return False
                else:
                    staging.append(interval)

        return True
