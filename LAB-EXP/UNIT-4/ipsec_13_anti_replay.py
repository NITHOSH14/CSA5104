# Anti-replay protection using sequence numbers

SEQUENCE_CACHE = {}


def check_packet(src, seq_no):
    last = SEQUENCE_CACHE.get(src, -1)
    if seq_no <= last:
        return False
    SEQUENCE_CACHE[src] = seq_no
    return True


if __name__ == '__main__':
    print(check_packet('10.0.0.1', 1))
    print(check_packet('10.0.0.1', 2))
    print(check_packet('10.0.0.1', 2))
