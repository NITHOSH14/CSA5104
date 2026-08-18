# Diffie-Hellman 1: Basic Key Exchange Implementation

p = 23
g = 5

alice_private = 4
bob_private = 3

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

shared_alice = pow(bob_public, alice_private, p)
shared_bob = pow(alice_public, bob_private, p)

print('Prime p:', p)
print('Generator g:', g)
print('Alice public key:', alice_public)
print('Bob public key:', bob_public)
print('Alice shared secret:', shared_alice)
print('Bob shared secret:', shared_bob)
print('Keys match:', shared_alice == shared_bob)
