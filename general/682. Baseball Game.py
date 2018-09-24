def calPoints(ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    total = []
    for i in ops:
        if i == 'D':
            total.append(2 * total[-1])
        elif i == 'C':
            total.pop()
        elif i == '+':
            total.append(total[-1] + total[-2])
        else:
            total.append(int(i))
    return sum(total)
