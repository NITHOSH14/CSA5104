import hashlib
import time


algorithms = ['md5', 'sha1', 'sha256', 'sha384', 'sha512']


def digest_for(algorithm: str, data: bytes) -> str:
    return hashlib.new(algorithm, data).hexdigest()


if __name__ == '__main__':
    text = 'This is a sample message for comparing hash algorithm performance. ' * 2000
    data = text.encode('utf-8')

    print(f"{'Algorithm':<12} {'Digest Length':<15} {'Time (s)':<12} {'Digest':<70}")
    for alg in algorithms:
        start = time.perf_counter()
        digest = digest_for(alg, data)
        elapsed = time.perf_counter() - start
        print(f"{alg:<12} {len(digest):<15} {elapsed:<12.8f} {digest:<70}")

    print('\nInterpretation:')
    print('Digest size increases with stronger security level, and execution time varies slightly by algorithm.')
