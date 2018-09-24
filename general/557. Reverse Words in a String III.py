# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = b = ""
        j = 0
        s = s + " "
        for i, ch in enumerate(s):
            if ch is " ":
                b = s[j:i]
                b = b[::-1]
                a = a + b + " "
                j = i + 1
        return a[0:-1]


s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))