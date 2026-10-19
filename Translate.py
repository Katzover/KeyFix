# Translates the text from english to hebrew or backwards based on keyboards mapping

EN_TO_HE = {"q": "/", "w": "'", "e": "ק", "r": "ר", "t": "א", "y": "ט", "u": "ו", "i": "ן", "o": "ם", "p": "פ", "[": "]", "]": "[", "a": "ש", "s": "ד", "d": "ג", "f": "כ", "g": "ע", "h": "י", "j": "ח", "k": "ל", "l": "ך", ";": "ף", "'": ",", "z": "ז", "x": "ס", "c": "ב", "v": "ה", "b": "נ", "n": "מ", "m": "צ", ",": "ת", ".": "ץ", "/": "."}

HE_TO_EN = {v: k for k, v in EN_TO_HE.items()}

def TranslateToHe(text):
    return "".join([EN_TO_HE.get(x, x) for x in text]).strip()

def TranslateToEn(text):
    return "".join([HE_TO_EN.get(x, x) for x in text]).strip()