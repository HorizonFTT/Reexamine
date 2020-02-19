import random

if __name__ == "__main__":
    path = 'org_2012.dat'
    data = [random.randint(-100, 100) for i in range(100)]
    with open(path, 'wb') as f:
        for i in data:
            b = i.to_bytes(4, 'little', signed=True)
            f.write(b)
