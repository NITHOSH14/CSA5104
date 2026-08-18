# Blowfish 2: Blowfish Decryption

from Crypto.Cipher import Blowfish


if __name__ == '__main__':
    key = b'SecretKey123'
    ciphertext = bytes.fromhex('3f90d410c4e47b3d')
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).rstrip(b' ')
    print('Ciphertext:', ciphertext.hex())
    print('Key:', key.decode())
    print('Original plaintext:', plaintext.decode())
