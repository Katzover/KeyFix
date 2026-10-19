# Goes through every word in both hebrew and english and checks whether a word typed exists in one but not the other
from locale import getdefaultlocale
from english_words import get_english_words_set
import Translate

with open("Hebrew.txt", encoding="utf-8") as he:
    HEBREW_SET = set(he.read().strip().lower().split("\n"))

ENGLISH_SET = get_english_words_set(['web2'], lower=True)


def Lookup(word):
    word = word.strip().lower()


    # English to Hebrew
    if word in ENGLISH_SET or Translate.TranslateToEn(word) in ENGLISH_SET:
        if word in ENGLISH_SET: return word
        return Translate.TranslateToEn(word)

    # Hebrew to English
    elif word in HEBREW_SET or Translate.TranslateToHe(word) in HEBREW_SET:
        if word in ENGLISH_SET: return word
        return Translate.TranslateToHe(word)
        

    return None
