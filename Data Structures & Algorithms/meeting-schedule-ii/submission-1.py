"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted([x.start for x in intervals])
        ends = sorted([x.end for x in intervals])


        s, e, meetingsMax, count = 0,0,0,0

        while s < len(starts) and e < len(ends):
            if starts[s] < ends[e]:
                s += 1
                count += 1
            else:
                e +=1
                count -= 1
            meetingsMax = max(meetingsMax, count)
        
        return meetingsMax
        
            