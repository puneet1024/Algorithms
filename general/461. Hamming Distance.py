
def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    return bin(x^y).count('1')

# or return len([i for i in bin(x^y) if i=='1'])

print(hammingDistance(2,5))