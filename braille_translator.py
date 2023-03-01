import tkinter as tk
from typing import Any


# contractions dictionary was converted to a list of tuples.
# (if left as a dictionary, dict.items() would've returned flipped key and value).
BRAILLE_CONTRACTIONS_LIST = [
    ('altogether', '⠁⠇⠞'), ('conceiving', '⠒⠉⠑⠊⠧⠔⠛'), ('perceiving', '⠏⠻⠉⠑⠊⠧⠔⠛'),
    ('themselves', '⠮⠍⠧⠎'), ('yourselves', '⠽⠗⠧⠎'), ('according', '⠁⠉'), ('afternoon', '⠁⠋⠝'),
    ('afterward', '⠁⠋⠺'), ('character', '⠐⠡'), ('declaring', '⠙⠉⠇⠛'), ('deceiving', '⠙⠑⠉⠑⠊⠧⠔⠛'),
    ('immediate', '⠊⠍⠍'), ('knowledge', '⠅'), ('necessary', '⠝⠑⠉'), ('ourselves', '⠳⠗⠧⠎'),
    ('receiving', '⠗⠑⠉⠑⠊⠧⠔⠛'), ('rejoicing', '⠗⠚⠉⠛'), ('although', '⠁⠇⠹'), ('children', '⠡⠝'),
    ('conceive', '⠒⠉⠧'), ('perceive', '⠏⠻⠉⠧'), ('question', '⠐⠟'), ('together', '⠞⠛⠗'),
    ('tomorrow', '⠞⠍'), ('yourself', '⠽⠗⠋'), ('against', '⠁⠛⠌'), ('already', '⠁⠇⠗'),
    ('because', '⠆⠉'), ('beneath', '⠆⠝'), ('between', '⠆⠞'), ('braille', '⠃⠗⠇'),
    ('declare', '⠙⠉⠇'), ('deceive', '⠙⠑⠉⠧'), ('herself', '⠓⠻⠋'), ('himself', '⠓⠍⠋'),
    ('neither', '⠝⠑⠊'), ('oneself', '⠕⠝⠑⠋'), ('perhaps', '⠏⠻⠓'), ('receive', '⠗⠑⠉⠧'),
    ('rejoice', '⠗⠚⠉'), ('through', '⠐⠹'), ('thyself', '⠹⠽⠋'), ('tonight', '⠞⠝'),
    ('across', '⠁⠉⠗'), ('almost', '⠁⠇⠍'), ('always', '⠁⠇⠺'), ('before', '⠆⠋'), ('behind', '⠆⠓'),
    ('beside', '⠆⠎'), ('beyond', '⠆⠽'), ('cannot', '⠸⠉'), ('either', '⠑⠊'), ('enough', '⠢'),
    ('father', '⠐⠋'), ('friend', '⠋⠗'), ('itself', '⠭⠋'), ('letter', '⠇⠗'), ('little', '⠇⠇'),
    ('mother', '⠐⠍'), ('myself', '⠍⠽⠋'), ('people', '⠏'), ('rather', '⠗'), ('should', '⠩⠙'),
    ('spirit', '⠸⠎'), ('about', '⠁⠃'), ('above', '⠁⠃⠧'), ('after', '⠁⠋'), ('again', '⠁⠛'),
    ('below', '⠆⠇'), ('blind', '⠃⠇'), ('child', '⠡'), ('could', '⠉⠙'), ('every', '⠑'),
    ('first', '⠋⠌'), ('great', '⠛⠗⠞'), ('ought', '⠐⠳'), ('quick', '⠟⠅'), ('quite', '⠟'),
    ('right', '⠐⠗'), ('shall', '⠩'), ('still', '⠌'), ('their', '⠸⠮'), ('there', '⠐⠮'),
    ('these', '⠘⠮'), ('those', '⠘⠹'), ('today', '⠞⠙'), ('under', '⠐⠥'), ('where', '⠐⠱'),
    ('which', '⠱'), ('whose', '⠘⠱'), ('world', '⠸⠺'), ('would', '⠺⠙'), ('young', '⠐⠽'),
    ('also', '⠁⠇'), ('ance', '⠁⠝⠉⠑'), ('ence', '⠢⠉⠑'), ('ever', '⠐⠑'), ('from', '⠋'),
    ('good', '⠛⠙'), ('have', '⠓'), ('here', '⠐⠓'), ('just', '⠚'), ('know', '⠐⠅'),
    ('less', '⠇⠑⠎⠎'), ('like', '⠇⠊⠅⠑'), ('lord', '⠐⠇'), ('many', '⠸⠍'), ('ment', '⠍⠢⠞'),
    ('more', '⠇'), ('much', '⠍⠡'), ('must', '⠍⠌'), ('name', '⠐⠝'), ('ness', '⠝⠑⠎⠎'),
    ('ound', '⠳⠝⠙'), ('ount', '⠳⠝⠞'), ('paid', '⠏⠙'), ('part', '⠐⠏'), ('said', '⠎⠙'),
    ('sion', '⠎⠊⠕⠝'), ('some', '⠐⠎'), ('such', '⠎⠡'), ('that', '⠞'), ('this', '⠹'),
    ('time', '⠐⠞'), ('tion', '⠞⠊⠕⠝'), ('upon', '⠘⠥'), ('very', '⠧'), ('went', '⠺⠢⠞'),
    ('were', '⠖'), ('will', '⠺'), ('with', '⠾'), ('word', '⠘⠺'), ('work', '⠐⠺'), ('your', '⠽⠗'),
    ('and', '⠯'), ('but', '⠃'), ('can', '⠉'), ('con', '⠒'), ('day', '⠐⠙'), ('dis', '⠲'),
    ('for', '⠿'), ('ful', '⠋⠥⠇'), ('had', '⠸⠓'), ('him', '⠓⠍'), ('his', '⠓⠊⠎'), ('ing', '⠔⠛'),
    ('its', '⠭⠎'), ('ity', '⠊⠞⠽'), ('not', '⠝'), ('one', '⠐⠕'), ('ong', '⠕⠝⠛'), ('out', '⠳'),
    ('the', '⠮'), ('was', '⠴'), ('you', '⠽'), ('ar', '⠜'), ('as', '⠵'), ('bb', '⠃⠃'), ('be', '⠆'),
    ('cc', '⠉⠉'), ('ch', '⠡'), ('do', '⠙'), ('ea', '⠑⠁'), ('ed', '⠫'), ('en', '⠢'), ('er', '⠻'),
    ('ff', '⠋⠋'), ('gg', '⠛⠛'), ('gh', '⠣'), ('go', '⠛'), ('in', '⠦'), ('it', '⠭'), ('of', '⠷'),
    ('ou', '⠳'), ('ow', '⠪'), ('sh', '⠩'), ('so', '⠎'), ('st', '⠌'), ('th', '⠹'), ('us', '⠥'),
    ('wh', '⠱')
]

# check for the first letter in braille contractions to be capitalized
CAPITALIZED_CONTRACTIONS_LIST: list[tuple[str, str | Any]] = [(word.capitalize(), tup[1]) for tup in
                                                              BRAILLE_CONTRACTIONS_LIST for word in tup]

BRAILLE_ALPHABET_CHARS = {
    " ": "⠀",
    "a": "⠁",
    "b": "⠃",
    "c": "⠉",
    "d": "⠙",
    "e": "⠑",
    "f": "⠋",
    "g": "⠛",
    "h": "⠓",
    "i": "⠊",
    "j": "⠚",
    "k": "⠅",
    "l": "⠇",
    "m": "⠍",
    "n": "⠝",
    "o": "⠕",
    "p": "⠏",
    "q": "⠟",
    "r": "⠗",
    "s": "⠎",
    "t": "⠞",
    "u": "⠥",
    "v": "⠧",
    "w": "⠺",
    "x": "⠭",
    "y": "⠽",
    "z": "⠵",
    '1': '⠁',
    '2': '⠃',
    '3': '⠉',
    '4': '⠙',
    '5': '⠑',
    '6': '⠋',
    '7': '⠛',
    '8': '⠓',
    '9': '⠊',
    '0': '⠚',
}

# isolate letters from the combined BRAILLE_ALPHABET_CHARS to be able to exclude numbers if user only inputs letters.
alphabet_only_dict = {k: v for k, v in BRAILLE_ALPHABET_CHARS.items() if not k.isdigit()}

BRAILLE_ALPHABET_CHARS_CAP = {
    "A": "⠁",
    "B": "⠃",
    "C": "⠉",
    "D": "⠙",
    "E": "⠑",
    "F": "⠋",
    "G": "⠛",
    "H": "⠓",
    "I": "⠊",
    "J": "⠚",
    "K": "⠅",
    "L": "⠇",
    "M": "⠍",
    "N": "⠝",
    "O": "⠕",
    "P": "⠏",
    "Q": "⠟",
    "R": "⠗",
    "S": "⠎",
    "T": "⠞",
    "U": "⠥",
    "V": "⠧",
    "W": "⠺",
    "X": "⠭",
    "Y": "⠽",
    "Z": "⠵",
}

# this dictionary is needed in case user ONLY inputs numbers.
BRAILLE_NUMBERS = {
    '1': '⠁',
    '2': '⠃',
    '3': '⠉',
    '4': '⠙',
    '5': '⠑',
    '6': '⠋',
    '7': '⠛',
    '8': '⠓',
    '9': '⠊',
    '0': '⠚',
}

BRAILLE_KEYBOARD_SYMBOLS = {
    '“': '⠦',
    '?': '⠦',
    "!": "⠮",
    "@": "⠐⠶⠃⠉",
    "#": "⠼⠃⠃",
    "$": "⠼⠃⠒",
    "%": "⠼⠃⠌",
    "^": "⠠⠎",
    "&": "⠠⠝",
    "*": "⠠⠢",
    "(": "⠠⠊",
    ")": "⠠⠛",
    "_": "⠠⠔",
    "-": "⠤",
    "+": "⠠⠖",
    "=": "⠔⠖",
    '/': '⠌',
    '”': '⠴',
    ',': '⠂',
    ';': '⠆',
    ':': '⠒',
    '.': '⠲',
    '\'': '⠄',
}


def english_to_braille(string):
    """Takes a string and returns the braille translation."""
    words = string.split()
    # store the final translated Braille string
    braille_string = ''
    for word in words:
        while True:
            # iterate through the word and look for any contractions in the word
            matched = False
            for contraction, braille in CAPITALIZED_CONTRACTIONS_LIST:
                if contraction in word:
                    # check if the current contraction appears in the current word
                    # if it does, add the Braille equivalent of the contraction to braille_string
                    braille_string += f'⠠{braille}'
                    # replace the matched contraction with an empty string in the current word
                    word = word.replace(contraction, "", 1)
                    matched = True
                    break
            for contraction, braille in BRAILLE_CONTRACTIONS_LIST:
                if contraction in word:
                    # check if the current contraction appears in the current word
                    # if it does, add the Braille equivalent of the contraction to braille_string
                    braille_string += braille
                    # replace the matched contraction with an empty string in the current word
                    word = word.replace(contraction, "", 1)
                    matched = True
                    break
            if not matched:
                break
        braille_word = ''
        number = ''
        for letter in word:
            if letter in alphabet_only_dict:
                braille_word += BRAILLE_ALPHABET_CHARS[letter]
            elif letter in BRAILLE_ALPHABET_CHARS_CAP:
                if word[0] in BRAILLE_ALPHABET_CHARS_CAP:
                    braille_word += f'⠠{BRAILLE_ALPHABET_CHARS_CAP[letter]}'
                else:
                    braille_word += BRAILLE_ALPHABET_CHARS_CAP[letter]
            elif letter in BRAILLE_KEYBOARD_SYMBOLS:
                braille_word += BRAILLE_KEYBOARD_SYMBOLS[letter]
            elif letter in BRAILLE_NUMBERS:
                number += BRAILLE_NUMBERS[letter]
        if not number == '':
            braille_word += f'⠼{number}'
        braille_string += braille_word
        # add a space character to braille_string to separate the Braille equivalent of each word
        braille_string += BRAILLE_ALPHABET_CHARS[' ']
    # remove the trailing space character from braille_string.
    return braille_string.strip()


class BrailleTranslatorApp(tk.Tk):
    """UI"""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("English to Braille Translator")
        self.geometry("350x350")
        self.resizable(False, False)

        self.entry = tk.Entry(self, font=("Helvetica", 14))
        self.entry.pack(pady=20)

        self.translate_button = tk.Button(self, text="Translate", command=self.translate)
        self.translate_button.pack()

        self.copy_button = tk.Button(self, text="Copy Braille Text", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=20)

        self.result = tk.Label(self, text="", wraplength=300, font=("Helvetica", 14))
        self.result.pack(pady=20)

    def translate(self):
        """Shows user input and translation on screen."""
        text = self.entry.get()
        braille = english_to_braille(text)
        self.result.config(text=braille)

    def copy_to_clipboard(self):
        """Allows translated text to be copied."""
        braille = self.result['text']
        self.clipboard_clear()
        self.clipboard_append(braille)


if __name__ == "__main__":
    app = BrailleTranslatorApp()
    app.mainloop()
