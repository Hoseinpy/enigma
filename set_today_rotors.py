import random, string, pickle

alphabet = string.ascii_lowercase

r1 = list(alphabet)
random.shuffle(r1)
r1 = ''.join(r1)

r2 = list(alphabet)
random.shuffle(r2)
r2 = ''.join(r2)

r3 = list(alphabet)
random.shuffle(r3)
r3 = ''.join(r3)

f = open('./today_rotors_state.enigma', 'wb')
pickle.dump((r1, r2, r3), f)