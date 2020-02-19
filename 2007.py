def get_primes(beg, end):
    origin = [1] * end
    origin[0], origin[1] = 0, 0

    for i in range(2, int(pow(end, 0.5)) + 1):
        if origin[i] == 1:
            origin[i * i::i] = [0] * len(origin[i * i::i])

    return [idx for idx, i in enumerate(origin) if i == 1 and idx >= beg]


def both_prime(n, prime_list):
    s = str(n)[::-1]
    return int(s) in prime_list


if __name__ == "__main__":
    path = 'result.txt'
    prime_list = get_primes(10, 1001)
    
    with open(path, 'w') as f:
        for p in prime_list:
            if both_prime(p, prime_list):
                f.write(str(p)+'\n')
