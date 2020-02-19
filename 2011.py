def get_primes(beg, end):
    origin = [1] * end
    origin[0], origin[1] = 0, 0

    for i in range(2, int(pow(end, 0.5)) + 1):
        if origin[i] == 1:
            origin[i * i::i] = [0] * len(origin[i * i::i])

    return [idx for idx, i in enumerate(origin) if i == 1 and idx >= beg]


def both_prime(s: str, prime_list):
    return int(s) in prime_list and int(s[::-1]) in prime_list


def meet_condition(num, prime_list):
    s = str(num)
    i = s[-2:]
    j = s[-3:-2]+s[-1:]
    return num in prime_list and both_prime(i, prime_list) and both_prime(j, prime_list)


if __name__ == "__main__":
    prime_list = get_primes(10, 10000)
    
    for i in range(1000, 10000):
        if meet_condition(i, prime_list):
            print(i)
