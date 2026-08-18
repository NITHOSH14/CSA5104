# Diffie-Hellman 2: Secure Chat Simulation

import hashlib

p = 23
g = 5

users = {'alice': 6, 'bob': 15}
public = {name: pow(g, priv, p) for name, priv in users.items()}
shared = {name: pow(public['bob' if name == 'alice' else 'alice'], priv, p) for name, priv in users.items()}

print('Alice public key:', public['alice'])
print('Bob public key:', public['bob'])
print('Alice shared key:', shared['alice'])
print('Bob shared key:', shared['bob'])

key = hashlib.sha256(str(shared['alice']).encode()).hexdigest()
message = 'Secure message from Alice'
# simple XOR-encrypted form for demonstration
cipher = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(message))
plain = ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(cipher))
print('Encrypted message:', cipher.encode('unicode_escape'))
print('Recovered message:', plain)
