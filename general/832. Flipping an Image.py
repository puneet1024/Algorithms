
def flipAndInvertImage(A):
    """
    :type A: List[List[int]]
    :rtype: List[List[int]]
    """
    rev_ret = []
    for row in A:
        row_ret = [abs(x-1) for x in row[::-1]]
        rev_ret.append(row_ret)
    return rev_ret

print(flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))