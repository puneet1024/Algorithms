
def numJewelsInStones( J, S):
    """
    :type J: str
    :type S: str
    :rtype: int
    """
    count =0
    for i in range(len(S)):
        if S[i] in J:
            count+=1
    return count


print(numJewelsInStones('aA','aaaAAAabcd'))