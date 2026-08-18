state = {}


def process_packet(connection_id, flag):
    current = state.get(connection_id, 'CLOSED')
    if flag == 'SYN' and current == 'CLOSED':
        state[connection_id] = 'ESTABLISHED'
        return 'ALLOWED'
    if flag == 'FIN' and current == 'ESTABLISHED':
        state[connection_id] = 'CLOSED'
        return 'ALLOWED'
    return 'BLOCKED'


if __name__ == '__main__':
    print(process_packet('A', 'SYN'))
    print(process_packet('A', 'FIN'))
