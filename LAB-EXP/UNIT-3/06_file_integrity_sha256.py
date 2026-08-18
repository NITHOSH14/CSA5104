import hashlib
import os


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            h.update(chunk)
    return h.hexdigest()


if __name__ == '__main__':
    file_path = input('Enter file path: ').strip().strip('"')
    if not os.path.exists(file_path):
        print('File not found!')
    else:
        original_hash = sha256_file(file_path)
        print('Original SHA-256:', original_hash)

        print('\nModify the file now and press Enter when done...')
        input()

        new_hash = sha256_file(file_path)
        if original_hash == new_hash:
            print('Verification: File has not changed.')
        else:
            print('Verification: File has been altered!')
            print('Updated SHA-256:', new_hash)
