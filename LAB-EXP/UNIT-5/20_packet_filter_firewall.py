rules = {
    'allow': [(80, 'ANY'), (443, 'ANY')],
    'block': [(22, '10.0.0.5')]
}


def packet_filter(src_ip, dst_port):
    if (dst_port, src_ip) in [(22, '10.0.0.5')]:
        return 'BLOCKED'
    if dst_port in [80, 443]:
        return 'ALLOWED'
    return 'BLOCKED'


if __name__ == '__main__':
    print(packet_filter('10.0.0.5', 22))
    print(packet_filter('192.168.1.10', 80))
