blocked_sites = ['badsite.com', 'malicious.test']


def proxy_firewall(url):
    if any(site in url for site in blocked_sites):
        return 'BLOCKED'
    return 'ALLOWED'


if __name__ == '__main__':
    print(proxy_firewall('https://goodsite.com'))
    print(proxy_firewall('https://badsite.com'))
