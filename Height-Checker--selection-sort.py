class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n=len(heights)
        count=0
        expected = sorted(heights)
        for i in range(n):
            if expected[i] != heights[i]:
                count+=1
        return count
        
n=input().strip("[]")
n=list(map(int,n.split(",")))
print(Solution().heightChecker(n))
