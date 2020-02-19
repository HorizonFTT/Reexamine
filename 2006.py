def get_primes(beg, end):
    origin = [1] * end
    origin[0], origin[1] = 0, 0

    for i in range(2, int(pow(end, 0.5)) + 1):
        if origin[i] == 1:
            origin[i * i::i] = [0] * len(origin[i * i::i])

    return [idx for idx, i in enumerate(origin) if i == 1 and idx >= beg]


def include_nine(n: int):
    s = str(n)

    for c in s:
        if c == '9':
            return True

    return False


if __name__ == "__main__":
    path = 'result'
    prime_list = get_primes(10, 1001)

    with open(path, 'w') as f:
        for p in prime_list:
            if not include_nine(p):
                f.write(str(p)+'\n')
