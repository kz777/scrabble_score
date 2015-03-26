def scrabble_score(word):
    st= 0
    word = word.lower()
    for key in word:
         st += score[key]
    return st