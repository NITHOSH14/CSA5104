p = 23
g = 5


def power_mod(base, exp, mod):
    return pow(base, exp, mod)


def diffie_hellman_demo():
    a = 6
    b = 15
    A = power_mod(g, a, p)
    B = power_mod(g, b, p)
    secret_a = power_mod(B, a, p)
    secret_b = power_mod(A, b, p)
    print('Public A:', A)
    print('Public B:', B)
    print('Shared secret:', secret_a)
    print('Match:', secret_a == secret_b)


if __name__ == '__main__':
    diffie_hellman_demo()
