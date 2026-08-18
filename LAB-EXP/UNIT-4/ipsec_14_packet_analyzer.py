# Identify AH and ESP headers in packet capture data


def analyze_packet(packet):
    if 'AH' in packet:
        return 'Authentication Header detected'
    if 'ESP' in packet:
        return 'Encapsulating Security Payload detected'
    return 'No IPSec header detected'


if __name__ == '__main__':
    sample = {'AH': 'next_header=TCP', 'payload': 'hello'}
    print(analyze_packet(sample))
