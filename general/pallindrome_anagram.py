#Check if any anagram of a given string is pallindrome or not


#Calculate the count of each syllable in a dictionary, if the count of more than one syllable is one, returns True, otherwise False
#anagram of 'abaaa' is pallindrome
#anagram of 'abcbca' is pallindrome
#anagram of 'xaampp' is not pallindrome

def pallin_ana(s):
    dicti = {}
    coun = 0

    for i in s:
        if i in dicti.keys():
            dicti[i] += 1
        else:
            dicti[i] = 1
    for k,v in dicti.items():
        if v%2 == 1:
            coun+=1
    return coun == 1
print(pallin_ana("geeksogeeks"))


# dicti = {'a':3 ,'b':9}
# print(sum(dicti.values()))