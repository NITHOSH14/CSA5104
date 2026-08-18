def detect_trojan(file_name, size, startup_enabled):
    score = 0
    if size > 5000000:
        score += 1
    if startup_enabled:
        score += 2
    if 'update' in file_name.lower():
        score += 2
    return score >= 3


if __name__ == '__main__':
    print('Suspicious:', detect_trojan('update_helper.exe', 7000000, True))
