# DES 4: DES File Decryption

from pathlib import Path
from Crypto.Cipher import DES


if __name__ == '__main__':
    enc = 'des_encrypted.bin'
    dec = 'des_decrypted.txt'
    key = b'abcdefgh'
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted = cipher.decrypt(Path(enc).read_bytes()).rstrip(b' ')
    Path(dec).write_bytes(decrypted)
    print('Decrypted file created:', dec)
