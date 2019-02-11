import string

import monoalph

with open("monoalph2.txt") as f:
    cipher = f.read()

freqs = monoalph.freq_analysis(cipher)
keya = {'X': 'e', 'Z': 't', 'C': 'i', 'M': 'h', 'V': 'a', 'R': 'm', 'P': 'y'}
tablea = str.maketrans(keya)
keyb = {'X': 'e', 'Z': 't', 'C': 'i', 'M': 'h', 'V': 'a', 'R': 'm', 'P': 'y', 'K': 'n', 'Q': 'k', 'J': 'r', 'E': 'v', 'O': 'l', 'L': 's', 'G': 'o', 'H': 'f', 'S': 'd', 'D': 'c', 'I': 'p', 'U': 'w', 'B': 'u', 'W': 'b', 'N': 'g'}
tableb = str.maketrans(keyb)

def transa():
    print(cipher.translate(tablea))

def transb():
    print(cipher.translate(tableb))

def pfreqs():
    print(monoalph.pretty_freqs(freqs))

def remcipherb():
    print(''.join(sorted(filter(lambda x: x not in keyb.keys(), string.ascii_uppercase), key=lambda x: freqs[x] if x in freqs else 0, reverse=True)))

def remclearb():
    print(''.join(sorted(filter(lambda x: x not in keyb.values(), string.ascii_lowercase), key=monoalph.en_freqs.get, reverse=True)))

transb()
#pfreqs()
#remcipherb()
#remclearb()