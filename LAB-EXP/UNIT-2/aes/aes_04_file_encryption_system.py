# AES 4: AES File Encryption System

from pathlib import Path
from Crypto.Cipher import AES


def pad(data: bytes) -> bytes:
    pad_len = 16 - (len(data) % 16)
    return data + bytes([pad_len]) * pad_len


def unpad(data: bytes) -> bytes:
    return data[:-data[-1]]


def encrypt_file(path, key, out_path):
    raw = Path(path).read_bytes()
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(pad(raw))
    Path(out_path).write_bytes(enc)


def decrypt_file(path, key, out_path):
    raw = Path(path).read_bytes()
    cipher = AES.new(key, AES.MODE_ECB)
    dec = cipher.decrypt(raw)
    Path(out_path).write_bytes(unpad(dec))


if __name__ == '__main__':
    source = 'aes_input.txt'
    encrypted = 'aes_encrypted.bin'
    restored = 'aes_restored.txt'
    key = b'0123456789abcdef'
    Path(source).write_text('AES file encryption demo.\nThe file will be encrypted and restored.', encoding='utf-8')
    encrypt_file(source, key, encrypted)
    decrypt_file(encrypted, key, restored)
    print('Restored matches original:', Path(source).read_text() == Path(restored).read_text())
