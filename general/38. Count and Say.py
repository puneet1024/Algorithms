class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        prev = "1"
        out = ""
        for i in range(1,n):
            count=1
            for j in range(len(prev)-1):
                if prev[j] == prev[j+1]:
                    count+=1
                else:
                    out+= str(count) + prev[j]
                    count=1
            out += str(count) + prev[-1]
            prev = out
            out = ""
        return prev

s = Solution()
s.countAndSay(4)