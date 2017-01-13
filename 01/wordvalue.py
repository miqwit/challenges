from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    all_words = []
    with open(DICTIONARY, 'r') as fd:
        all_words = filter(None, fd.read().split("\n"))
    return all_words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0

    for letter in word.upper():
        try:
            score += LETTER_SCORES[letter]
        except KeyError:
            pass  # Unknown letters value 0. Try/catch is faster than LETTER_SCORES.get(letter, 0)

    return score or 0

def max_word_value(dictionary=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not dictionary:
        dictionary = load_words()

    return max([(calc_word_value(word), word) for word in dictionary])[1]

if __name__ == "__main__":
    pass # run unittests to validate
