import string, pickle

alphabet = string.ascii_lowercase

f = open('./today_rotors_state.enigma', 'rb')
r1, r2, r3 = pickle.load(f)


def reflector(c):
    return alphabet[-alphabet.find(c) - 1]

def rotors_system(c):
    c1 = r1[alphabet.find(c)]
    c2 = r2[alphabet.find(c1)]
    c3 = r3[alphabet.find(c2)]
    ref = reflector(c3)
    c3 = alphabet[r3.find(ref)]
    c2 = alphabet[r2.find(c3)]
    c1 = alphabet[r1.find(c2)]
    
    return c1

def route_rotors(state):
    global r1, r2, r3
    r1 = r1[1:] + r1[0]
    if state % 26:
        r2 = r2[1:] + r2[0]
    if state % (26*26):
        r3 = r3[1:] + r3[0]

def main():
    plain = str(input('enter boss: '))
    cipher = ""
    state = 0
    
    for c in ''.join(plain.split()):
        state += 1
        cipher += rotors_system(c)
        route_rotors(state)
        
    return cipher


if __name__ == "__main__":
    ciphred = main()
    print(ciphred)