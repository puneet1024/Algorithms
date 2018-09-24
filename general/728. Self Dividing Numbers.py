def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """


#Append number <10 to the list and add those whose digits are individually divisible by the number
    ret = []

    for i in range(left, right + 1):
        if (i > 0 and i < 10):
            ret.append((i))
        else:
            n = i
            count = 0     #to count the number of divisible digits in a number
            while (i is not 0):
                d = i%10
                if(d is not 0 and ((n % d) == 0)):
                    i=i//10
                    count +=1
                else:
                    break
            if count == len(str(n)):
                ret.append(n)

    return ret


print(selfDividingNumbers(1, 22))

