class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        stopwords = ["!","?",",",".",";","'"," "]
        maxi = 0
        mc =""
        wc ={}
        for x in stopwords:
            paragraph = paragraph.replace(x," ")
        for each in paragraph.lower().split():
            if each not in banned:
                if each not in wc:
                    wc[each] = 1
                else:
                    wc[each]+=1
        for key,value in wc.items():
            if value > maxi:
                maxi = value
                mc = key
        return mc