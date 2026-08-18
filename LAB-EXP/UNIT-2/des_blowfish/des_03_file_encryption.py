# DES 3: DES File Encryption

from pathlib import Path
from Crypto.Cipher import DES


if __name__ == '__main__':
    src = 'des_input.txt'
    enc = 'des_encrypted.bin'
    Path(src).write_text('DES file encryption demonstration.', encoding='utf-8')
    key = b'abcdefgh'
    data = Path(src).read_bytes()
    padded = data + b' ' * ((8 - len(data) % 8) % 8)
    cipher = DES.new(key, DES.MODE_ECB)
    Path(enc).write_bytes(cipher.encrypt(padded))
    print('Encrypted file created:', enc)
