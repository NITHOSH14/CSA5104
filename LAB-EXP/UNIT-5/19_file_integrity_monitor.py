import hashlib, json, os


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            h.update(chunk)
    return h.hexdigest()


def monitor(folder):
    records = {}
    for root, _, files in os.walk(folder):
        for file in files:
            path = os.path.join(root, file)
            records[path] = sha256_file(path)
    return records


if __name__ == '__main__':
    state = monitor('.')
    print(json.dumps(state, indent=2)[:300])
