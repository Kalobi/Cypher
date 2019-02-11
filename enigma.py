reflector = dict(zip(range(0, 26), [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]))
scramblerI = dict(zip(range(0, 26), [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]))
scramblerII = dict(zip(range(0, 26), [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]))
scramblerIII = dict(zip(range(0, 26), [1, 3, 5, 7, 9, 11, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]))

plugboard = {0: 1, 18: 25, 20: 24, 6: 7, 11: 16, 4: 13}
mirr = {v: k for k, v in plugboard.items()}
plugboard.update(mirr)

rotors = [[scramblerII, 0], [scramblerI, 4], [scramblerIII, 1]]
#rotors = list(reversed(rotors))

cipher = "GYHRVFLRXY"

plain_nums = []

for c in cipher:
    c = ord(c) - ord('A')
#    for rotor in rotors: # rotation
#        rotor[1] = (rotor[1] + 1) % 26
    rotors[0][1] = (rotors[0][1] + 1) % 26 # rotation
    if c in plugboard: # feed through plugboard
        c = plugboard[c]
    for rotor in rotors: # feed through scramblers
        c = (rotor[0][(c + rotor[1]) % 26] - rotor[1]) % 26
    c = reflector[c] # reflect
    for rotor in reversed(rotors): # feed through scramblers backwards
        c = (next(key for key, value in rotor[0].items() if value == (c + rotor[1]) % 26) - rotor[1]) % 26
    if c in plugboard: # feed through plugboard again
        c = plugboard[c]
    plain_nums.append(c)

plain = ''.join(chr(c + ord('A')) for c in plain_nums)
print(plain)