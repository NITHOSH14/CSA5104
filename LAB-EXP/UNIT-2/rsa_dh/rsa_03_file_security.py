# RSA 3: RSA Encryption for Text File Security

from pathlib import Path
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt_file(input_path, output_path, public_key):
    data = Path(input_path).read_bytes()
    cipher = PKCS1_OAEP.new(public_key)
    block_size = 190
    encrypted = b''
    for i in range(0, len(data), block_size):
        encrypted += cipher.encrypt(data[i:i + block_size])
    Path(output_path).write_bytes(encrypted)
    print(f'Encrypted file saved to {output_path}')


def decrypt_file(input_path, output_path, private_key):
    data = Path(input_path).read_bytes()
    cipher = PKCS1_OAEP.new(private_key)
    block_size = 256
    decrypted = b''
    for i in range(0, len(data), block_size):
        decrypted += cipher.decrypt(data[i:i + block_size])
    Path(output_path).write_bytes(decrypted)
    print(f'Decrypted file saved to {output_path}')


if __name__ == '__main__':
    input_file = 'rsa_plaintext.txt'
    encrypted_file = 'rsa_ciphertext.bin'
    decrypted_file = 'rsa_restored.txt'

    Path(input_file).write_text('RSA file encryption example.\nThis file will be encrypted and decrypted.', encoding='utf-8')
    key = RSA.generate(1024)
    public_key = key.publickey()

    encrypt_file(input_file, encrypted_file, public_key)
    decrypt_file(encrypted_file, decrypted_file, key)

    print('Original content matches restored file:', Path(input_file).read_text() == Path(decrypted_file).read_text())
