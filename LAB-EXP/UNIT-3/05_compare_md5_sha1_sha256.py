import hashlib
import time


def measure_hash(name: str, data: bytes):
    start = time.perf_counter()
    digest = hashlib.new(name, data).hexdigest()
    elapsed = time.perf_counter() - start
    return digest, elapsed


if __name__ == '__main__':
    message = input('Enter a message: ')
    data = message.encode('utf-8')

    algorithms = ['md5', 'sha1', 'sha256']
    results = []

    for alg in algorithms:
        digest, elapsed = measure_hash(alg, data)
        results.append((alg.upper(), len(digest), elapsed, digest))

    print('\nHash Comparison Results:')
    print(f"{'Algorithm':<10} {'Digest Length':<15} {'Time (s)':<12} {'Digest':<70}")
    for alg, length, elapsed, digest in results:
        print(f"{alg:<10} {length:<15} {elapsed:<12.8f} {digest:<70}")

    print('\nObservation:')
    print('MD5 and SHA-1 are shorter and faster but weaker than SHA-256 for security-sensitive use.')
