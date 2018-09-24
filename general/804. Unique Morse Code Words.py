
def uniqueMorseRepresentations( words):
    """
    :type words: List[str]
    :rtype: int
    """
    dict_map = {
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."}

    m_words = []
    for word in words:
        m_word = ""
        for letter in word:
            m_word = m_word + dict_map[letter]
        if m_word not in m_words:
            m_words.append(m_word)
    return len(m_words)


print(uniqueMorseRepresentations(["hfdjshf","gidsa","fsdfaa","dsff"]))