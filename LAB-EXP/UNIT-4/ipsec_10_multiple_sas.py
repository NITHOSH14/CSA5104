# Multiple Security Associations for various sessions

SA_DB = {
    'session_a': {'spi': 1001, 'src': 'A', 'dst': 'B', 'proto': 'AH'},
    'session_b': {'spi': 1002, 'src': 'A', 'dst': 'C', 'proto': 'ESP'},
    'session_c': {'spi': 1003, 'src': 'D', 'dst': 'E', 'proto': 'ESP'},
}


def get_sa(session_name):
    return SA_DB.get(session_name)


if __name__ == '__main__':
    for name in ['session_a', 'session_b', 'session_c']:
        print(name, '->', get_sa(name))
