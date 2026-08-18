# RC5 4: RC5 File Encryption and Decryption

from pathlib import Path
from rc5_01_encryption_decryption import encrypt_block, decrypt_block


def file_encrypt(src_path, dst_path, key, rounds=12):
    raw = Path(src_path).read_bytes()
    padded = raw.ljust((len(raw) + 7) // 8 * 8, b' ')
    out = b''
    for i in range(0, len(padded), 8):
        out += encrypt_block(padded[i:i + 8], key, rounds)
    Path(dst_path).write_bytes(out)
    print('Encrypted file saved:', dst_path)


def file_decrypt(src_path, dst_path, key, rounds=12):
    raw = Path(src_path).read_bytes()
    out = b''
    for i in range(0, len(raw), 8):
        out += decrypt_block(raw[i:i + 8], key, rounds)
    Path(dst_path).write_bytes(out.rstrip(b' '))
    print('Decrypted file saved:', dst_path)


if __name__ == '__main__':
    src = 'rc5_input.txt'
    enc = 'rc5_encrypted.bin'
    dec = 'rc5_decrypted.txt'
    Path(src).write_text('RC5 file encryption demo.\nThis input will be encrypted and restored.', encoding='utf-8')
    file_encrypt(src, enc, 'SecretKey123', 12)
    file_decrypt(enc, dec, 'SecretKey123', 12)
    print('Restored content matches original:', Path(src).read_text() == Path(dec).read_text())
