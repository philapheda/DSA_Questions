class Solution(object):
    def minProcessingTime(self, processorTime, tasks):
        tasks= list(reversed(sorted(tasks)))
        processorTime.sort()
        max_time = 0
        for i in range(len(processorTime)):
            max_time = max(max_time, processorTime[i]+tasks[4*(i)])
        return max_time
        """
        :type processorTime: List[int]
        :type tasks: List[int]
        :rtype: int
        """
        