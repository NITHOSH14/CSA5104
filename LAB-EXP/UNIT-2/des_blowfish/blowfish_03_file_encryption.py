# Blowfish 3: Blowfish File Encryption

from pathlib import Path
from Crypto.Cipher import Blowfish


if __name__ == '__main__':
    src = 'blowfish_input.txt'
    enc = 'blowfish_encrypted.bin'
    Path(src).write_text('Blowfish file encryption example.', encoding='utf-8')
    key = b'SecretKey123'
    data = Path(src).read_bytes() + b' ' * ((8 - len(Path(src).read_bytes()) % 8) % 8)
    cipher = Blowfish.new(key, Blowfish.MODE_ECB)
    Path(enc).write_bytes(cipher.encrypt(data))
    print('Encrypted file created:', enc)
