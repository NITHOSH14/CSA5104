# Diffie-Hellman 5: Man-in-the-Middle Attack Simulation

p = 23
g = 5

alice_private = 4
bob_private = 3
mallory_private = 7

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)
mallory_public = pow(g, mallory_private, p)

# normal exchange
shared_alice = pow(bob_public, alice_private, p)
shared_bob = pow(alice_public, bob_private, p)

# MITM exchange
mallory_alice = pow(mallory_public, alice_private, p)
mallory_bob = pow(mallory_public, bob_private, p)

print('Normal shared secret (Alice/Bob):', shared_alice)
print('Normal shared secret (Bob/Alice):', shared_bob)
print('Mallory intercepts and shares a key with Alice:', mallory_alice)
print('Mallory intercepts and shares a key with Bob:', mallory_bob)
print('Attack status: Both users believe they have a private channel, but Mallory can read their messages.')
print('Mitigation: Use digital certificates or authenticated key exchange to verify identities.')
