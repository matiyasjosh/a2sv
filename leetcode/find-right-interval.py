class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        ans  = []

        values = [interval[0] for interval in intervals]
        temp = sorted(values)


        for interval in intervals:
            start, end = 0, len(temp) - 1
            index = -1

            
            while start <= end:
                mid = (start + end) // 2

                if interval[1] > temp[mid]:
                    start = mid + 1
                elif interval[1] <= temp[mid]:
                    index = values.index(temp[mid])
                    end = mid - 1

            ans.append(index)

        return ans