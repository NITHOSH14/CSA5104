# Diffie-Hellman 3: Multiple Users Simulation

p = 101
g = 2

participants = {'A': 5, 'B': 12, 'C': 18}
public_keys = {name: pow(g, priv, p) for name, priv in participants.items()}

print('Public keys:')
for name, value in public_keys.items():
    print(name, value)

for a, b in [('A', 'B'), ('A', 'C'), ('B', 'C')]:
    shared = pow(public_keys[b], participants[a], p)
    print(f'Shared secret between {a} and {b}: {shared}')
