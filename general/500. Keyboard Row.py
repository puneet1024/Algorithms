def findWords( words):
    """
    :type words: List[str]
    :rtype: List[str]
    """
    a = 'qwertyuiop'
    b = 'asdfghjkl'
    c = 'zxcvbnm'
    result = []
    count1, count2, count3 = 0, 0, 0
    for i in words:
        d = set(i.lower())
        print(d)
        for j in d:
            if j in a:
                count1 += 1
            elif j in b:
                count2 += 1
            elif j in c:
                count3 += 1
        if count1 == len(d) or count2 == len(d) or count3 == len(d):
            result.append(i)
        count1, count2, count3 = 0, 0, 0
    return result

print(findWords(["Hello", "Alaska", "Dad", "Peace","Qwerty"]))