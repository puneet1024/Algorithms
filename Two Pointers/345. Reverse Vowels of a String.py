class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowel = 'aeiouAEIOU'
        start = 0
        end = len(s)-1
        words = list(s)
        while start < end:
            if words[start] in vowel and words[end] in vowel:
                words[start],words[end] = words[end],words[start]
                start +=1
                end -=1
            elif words[start] in vowel:
                end -=1
            elif words[end] in vowel:
                start +=1
            else:
                start += 1
                end -= 1
        return ''.join(words)

s = Solution()
print(s.reverseVowels("hello"))