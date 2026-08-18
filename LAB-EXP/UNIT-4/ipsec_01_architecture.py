

from dataclasses import dataclass

@dataclass
class SecurityAssociation:
    spi: int
    src: str
    dst: str
    protocol: str
    mode: str
    key: str


def show_ipsec_architecture():
    print('IPSec Architecture Overview')
    print('1. IKE/ISAKMP: establishes security policy and negotiates keys')
    print('2. SA Database: stores Security Associations (SPI, src, dst, protocol, mode)')
    print('3. AH: provides integrity and origin authentication')
    print('4. ESP: provides confidentiality + integrity + authentication')
    print('5. IP packet processing: match SA -> apply AH/ESP -> forward packet')
    print('6. Peer receives packet: lookup SA -> verify/decrypt -> deliver payload')
    sa = SecurityAssociation(1001, '10.0.0.1', '10.0.0.2', 'ESP', 'Tunnel', 'shared123')
    print(f'Example SA: {sa}')


if __name__ == '__main__':
    show_ipsec_architecture()
