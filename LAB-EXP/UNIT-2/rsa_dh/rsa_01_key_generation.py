# RSA 1: Key Generation, Encryption and Decryption

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def main():
    message = input('Enter message: ').encode()
    key = RSA.generate(1024)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    ciphertext = cipher.encrypt(message)
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ciphertext)

    print('\nPublic Key:', public_key.n)
    print('Private Key:', key.d)
    print('Encrypted Ciphertext (hex):', ciphertext.hex())
    print('Decrypted Message:', decrypted.decode())


if __name__ == '__main__':
    main()
