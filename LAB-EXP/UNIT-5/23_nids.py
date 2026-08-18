rules = [
    {'protocol': 'TCP', 'port': 22},
    {'protocol': 'ICMP', 'payload': 'ping'}
]


def detect_attack(packet):
    for rule in rules:
        if packet.get('protocol') == rule['protocol'] and packet.get('port') == rule.get('port'):
            return 'ALERT'
        if packet.get('protocol') == rule['protocol'] and packet.get('payload') == rule.get('payload'):
            return 'ALERT'
    return 'NORMAL'


if __name__ == '__main__':
    packet = {'protocol': 'TCP', 'port': 22}
    print(detect_attack(packet))
