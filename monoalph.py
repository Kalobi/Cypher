import string

class Caesar():
    
    def __init__(self, shift):
        self.shift = shift
    
    def __getitem__(self, plain):
        if ord('A') <= plain <= ord('Z'):
            cipher = plain + self.shift
            if cipher > ord('Z'):
                cipher = cipher - 26
            return cipher
        elif ord('a') <= plain <= ord('z'):
            cipher = plain + self.shift
            if cipher > ord('z'):
                cipher = cipher - 26
            return cipher
        raise LookupError

def freq_analysis(text, absolute=False):
    freqs = {}
    text = ''.join(filter(lambda char: char in string.ascii_letters, text))
    for char in text:
        if char not in freqs:
            freqs[char] = 1
        else:
            freqs[char] += 1
    total = len(text)
    if not absolute:
        for key in freqs.keys():
            freqs[key] /= total
    return freqs

def pretty_freqs(freqs):
    return '\n'.join(f"{key}: {freqs[key]:.2%}"
                     for key in sorted(freqs.keys(), key=freqs.get, reverse=True))

en_freqs = dict(zip("etaonisrhldcupfmwybgvkqxjz", [0.123, 0.096, 0.081, 0.079, 0.072, 0.072, 0.066, 0.06, 0.051, 0.04, 0.037, 0.032, 0.031, 0.023, 0.023, 0.023, 0.02, 0.019, 0.016, 0.016, 0.009, 0.005, 0.002, 0.002, 0.001, 0.001]))
_upper_en = {key.upper(): en_freqs[key] for key in en_freqs.keys()}
en_freqs.update(_upper_en)