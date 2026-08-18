# Blowfish 4: Blowfish File Decryption

from pathlib import Path
from Crypto.Cipher import Blowfish


if __name__ == '__main__':
    enc = 'blowfish_encrypted.bin'
    dec = 'blowfish_decrypted.txt'
    key = b'SecretKey123'
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    decrypted = cipher.decrypt(Path(enc).read_bytes()).rstrip(b' ')
    Path(dec).write_bytes(decrypted)
    print('Decrypted file created:', dec)
