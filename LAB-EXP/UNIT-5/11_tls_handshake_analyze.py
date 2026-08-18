from scapy.all import rdpcap


def analyze_pcap(file_name):
    packets = rdpcap(file_name)
    for pkt in packets:
        if 'TLS' in pkt.summary() or 'ClientHello' in pkt.summary() or 'ServerHello' in pkt.summary():
            print(pkt.summary())


if __name__ == '__main__':
    print('Example: analyze_pcap("capture.pcap")')
