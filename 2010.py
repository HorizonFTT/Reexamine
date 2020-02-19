def get_nums(path):
    result = []

    with open(path, 'rb') as f:
        data = f.read()

        for i in range(len(data)//4):
            beg = 4 * i
            end = beg + 4
            b = data[beg:end]
            num = int.from_bytes(b, 'little')

            if num == 0:
                print(f'n = {i}')
                break
            result.append(num)

    return result


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(pow(n, 0.5)) + 1):
        if n % i == 0:
            return False

    return True


def get_max_prime(nums):
    for i in reversed(nums):
        if is_prime(i):
            return i

    return None


if __name__ == "__main__":
    path = 'data.txt'
    nums = get_nums(path)

    print('max of nums:', max(nums))
    print('min of nums:', min(nums))
    print('max of primes:', get_max_prime(nums))

    nums.sort(reverse=True)
    length = len(nums)//3
    l = nums[length:2*length]
    print('max of mid_seg:', max(l))
    print('min of mid_seg:', min(l))

