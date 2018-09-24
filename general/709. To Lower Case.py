class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        a = ""
        for ch in str:
            if ch.isupper():
                ch = chr(ord(ch) + 32)
                a = a + ch
            else:
                a = a + ch
        return a


