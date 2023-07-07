# words = ["word", "world", "row"]
# order = "worldabcefghijkmnpqstuvxyz"

words = ["habito", "hacer", "lectura", "sonreir"]
order = "hlabcdfgijkmnopqrstuvwxyz"

# words = ["conocer", "cono"]
# order = "abcdefghijkmnopqrstuvwxyz"


def isAlienSorted(words, order):
    for i in range(len(words) - 1):
        print(words[i], words[i+1])
        if two_words(words[i], words[i + 1], order):
            return False
    return True


def two_words(word1, word2, order):
    try:
        index1 = order.index(word1[0])
    except:
        return False

    try:
        index2 = order.index(word2[0])
    except:
        return True

    if index1 < index2:
        return False
    if index1 > index2:
        return True
    return two_words(word1[1:], word2[1:], order)

print("empiezo...")
isAlienSorted(words, order)
print("termino...")
