def statistics(path: str):
    d = {}
    with open(path, 'r') as f:
        for c in f.read():
            c = c.lower()
            if not c.isalpha():
                continue
            if d.get(c):
                d[c] += 1
            else:
                d[c] = 1
    return d


if __name__ == "__main__":
    path = 'test.txt'
    d = statistics(path)
    for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True):
        print(f'{k}: {v}')
