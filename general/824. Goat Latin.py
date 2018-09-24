def toGoatLatin(S):
    """
    :type S: str
    :rtype: str
    """
    l = S.split(" ")
    li = []
    for value, i in enumerate(l, 1):
        if i[0] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'O', 'I', 'U'}:
            i = i + 'ma'
        else:
            i = i[1:] + i[0] + 'ma'
        i = i  + 'a' * value
        li.append(i)
    s = (" ").join(li)
    return s


print(toGoatLatin("I speak Goat Latin"))