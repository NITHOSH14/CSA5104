from scapy.all import rdpcap


def summarize_pcap(file_name):
    packets = rdpcap(file_name)
    tcp = sum(1 for p in packets if 'TCP' in p.summary())
    udp = sum(1 for p in packets if 'UDP' in p.summary())
    tls = sum(1 for p in packets if 'TLS' in p.summary())
    print(f'TCP: {tcp}, UDP: {udp}, TLS: {tls}')


if __name__ == '__main__':
    print('Use a .pcap file to run: summarize_pcap("capture.pcap")')
