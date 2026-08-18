# Manual key configuration for IPSec

MANUAL_KEYS = {
    'AH': 'manual_ah_key_123',
    'ESP': 'manual_esp_key_456',
}


def get_manual_key(protocol):
    return MANUAL_KEYS.get(protocol)


if __name__ == '__main__':
    print('AH key:', get_manual_key('AH'))
    print('ESP key:', get_manual_key('ESP'))
