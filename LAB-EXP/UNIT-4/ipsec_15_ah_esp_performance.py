# Compare AH and ESP overhead and processing time
import time


def measure(func, payload):
    t0 = time.perf_counter()
    func(payload)
    t1 = time.perf_counter()
    return t1 - t0


def ah_overhead(payload):
    return len(payload) + 16


def esp_overhead(payload):
    return len(payload) + 32


if __name__ == '__main__':
    payload = 'A' * 1000
    print('AH overhead bytes:', ah_overhead(payload))
    print('ESP overhead bytes:', esp_overhead(payload))
    print('AH time:', measure(ah_overhead, payload))
    print('ESP time:', measure(esp_overhead, payload))
