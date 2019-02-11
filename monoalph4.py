import string
import re

import monoalph

with open("monoalph4.txt") as f:
    cipher = f.read()

freqs = monoalph.freq_analysis(cipher)
key = {'J': 'e', 'K': 't', 'E': 'h'}
table = str.maketrans(key)

clear = cipher.translate(table)

def pfreqs():
    print(monoalph.pretty_freqs(freqs))

def remcipher():
    print(''.join(sorted(filter(lambda x: x not in key.keys(), string.ascii_uppercase), key=lambda x: freqs[x] if x in freqs else 0, reverse=True)))

def remclear():
    print(''.join(sorted(filter(lambda x: x not in key.values(), string.ascii_lowercase), key=monoalph.en_freqs.get, reverse=True)))

def pthes():
    thes = re.findall("..e", cipher.translate(table))
    the_freqs = {}
    for the in thes:
        if the in the_freqs.keys():
            the_freqs[the] += 1
        else:
            the_freqs[the] = 1
    print(the_freqs)

#clear = clear.replace("the", " the ")
print(clear)
#pfreqs()
#remcipher()
#remclear()