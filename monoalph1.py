import monoalph


with open("monoalph1.txt") as f:
    cipher = f.read()

given = {ord('B'): 'o', ord('D'): 'g', ord('G'): 't', ord('P'): 'e', ord('R'): 's', ord('Z'): 'd'}
test = given

test[ord('X')] = 'm'
test[ord('W')] = 'i'
test[ord('M')] = 'u'
test[ord('S')] = 'v'
test[ord('T')] = 'h'
test[ord('H')] = 'a'
test[ord('Q')] = 'n'
test[ord('K')] = 'l'
test[ord('L')] = 'y'
test[ord('N')] = 'p'
test[ord('U')] = 'w'
test[ord('I')] = 'b'
test[ord('O')] = 'r'
test[ord('F')] = 'c'

print(cipher.translate(test))
#freqs = monoalph.freq_analysis(cipher)
#print(monoalph.pretty_freqs(freqs))