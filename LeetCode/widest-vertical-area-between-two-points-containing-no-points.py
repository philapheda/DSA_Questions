class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        max_width = 0
        x = []
        for i in points:
            xp,yp = i
            x.append(xp)
        x.sort()
        for i in range(len(points)-1):
            width = x[i+1] - x[i]
            max_width = max(max_width,width)
        return max_width        