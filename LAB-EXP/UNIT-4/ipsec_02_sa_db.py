# Security Association database simulation
# Stores SA entries and performs lookup for inbound packets.

SA_DB = {
    ('10.0.0.1', '10.0.0.2', 5001): {'proto': 'AH', 'mode': 'Transport', 'spi': 5001, 'key': 'ahkey1'},
    ('10.0.0.1', '10.0.0.2', 5002): {'proto': 'ESP', 'mode': 'Tunnel', 'spi': 5002, 'key': 'espkey1'},
    ('10.0.0.3', '10.0.0.4', 6001): {'proto': 'ESP', 'mode': 'Transport', 'spi': 6001, 'key': 'espkey2'},
}


def lookup_sa(src, dst, spi):
    return SA_DB.get((src, dst, spi), None)


def simulate_packet_lookup(packet):
    sa = lookup_sa(packet['src'], packet['dst'], packet['spi'])
    if sa:
        return {'status': 'matched', 'sa': sa}
    return {'status': 'no match'}


if __name__ == '__main__':
    packets = [
        {'src': '10.0.0.1', 'dst': '10.0.0.2', 'spi': 5001},
        {'src': '10.0.0.5', 'dst': '10.0.0.6', 'spi': 9999},
    ]
    for pkt in packets:
        print(simulate_packet_lookup(pkt))
