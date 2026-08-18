# DES 2: DES Decryption

from Crypto.Cipher import DES


if __name__ == '__main__':
    key = b'13345779'
    ciphertext = bytes.fromhex('85E813540F0AB405')
    cipher = DES.new(key, DES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext).rstrip(b' ')
    print('Ciphertext:', ciphertext.hex())
    print('Key:', key)
    print('Recovered plaintext:', plaintext.decode())
