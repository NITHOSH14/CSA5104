# IPSec transport and tunnel mode simulation


def transport_mode(packet):
    return {'mode': 'Transport', 'outer_ip_header': 'original IP header preserved', 'payload': packet}


def tunnel_mode(packet):
    return {'mode': 'Tunnel', 'outer_ip_header': 'new IP header added', 'payload': packet}


if __name__ == '__main__':
    sample = {'src': '10.0.0.1', 'dst': '10.0.0.2', 'payload': 'secure data'}
    print(transport_mode(sample))
    print(tunnel_mode(sample))
