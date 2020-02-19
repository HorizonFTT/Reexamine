def get_primes(n):
    origin = [1] * n
    origin[0], origin[1] = 0, 0

    for i in range(2, int(pow(n, 0.5)) + 1):
        if origin[i] == 1:
            origin[i * i::i] = [0] * len(origin[i * i::i])
            
    return [idx for idx, i in enumerate(origin) if i == 1]


def sum_of_prime(n: int):
    if n < 2:
        return []

    prime_list = get_primes(n + 1)
    result = []

    i = -1
    while True:
        p = prime_list[i]
        if n > p + 1 or n == p:
            result.append(str(p))
            n -= p
        else:
            i -= 1
        if n == 0:
            break

    return reversed(result)


if __name__ == "__main__":
    n = int(input())
    result = sum_of_prime(n)
    print(' + '.join(result)+' = '+str(n))
