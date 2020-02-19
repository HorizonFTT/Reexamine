import random

if __name__ == "__main__":
    path = 'data.txt'
    n = random.randint(1, 2047)
    data = [random.randint(0, i) + 1 if i < n else 0 for i in range(2048)]
    with open(path, 'wb') as f:
        for i in data:
            b = i.to_bytes(4, 'little')
            f.write(b)

    print(f'n = {n}')
