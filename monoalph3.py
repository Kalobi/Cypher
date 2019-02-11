import string

import monoalph

with open("monoalph3.txt") as f:
    cipher = f.read()

freqs = monoalph.freq_analysis(cipher)
#key = {'C': 'e', 'A': 't', 'B': 'h', 'H': 'a', 'D': 'r'}
key = {'C': 'e', 'A': 't', 'B': 'h', 'H': 'a', 'D': 'r', 'E': 'i', 'F': 's', 'G': 'v', 'L': 'o', 'K': 'w', 'I': 'f', 'M': 'n', 'J': 'l', 'R': 'p', 'N': 'b', 'O': 'd', 'X': 'g', 'P': 'u', 'T': 'c', 'Q': 'm', 'U': 'k', 'V': 'y', 'W': 'q', 'S': 'j'}
table = str.maketrans(key)

def trans():
    print(cipher.translate(table))

def pfreqs():
    print(monoalph.pretty_freqs(freqs))

def remcipher():
    print(''.join(sorted(filter(lambda x: x not in key.keys(), string.ascii_uppercase), key=lambda x: freqs[x] if x in freqs else 0, reverse=True)))

def remclear():
    print(''.join(sorted(filter(lambda x: x not in key.values(), string.ascii_lowercase), key=monoalph.en_freqs.get, reverse=True)))

trans()
#pfreqs()
#remcipher()
#remclear()