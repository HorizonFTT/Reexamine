def handle_num(num: str):
    s = ''
    for c in num:
        if c != ' ':
            s += c
    if s[:1] == '0':
        s = '0o'+s[1:]
        return int(s, 8)
    return int(s)

def handle_article(path_from, path_to):
    with open(path_from, 'r') as f_in:
        with open(path_to, 'w') as f_out:
            for n in f_in.read().split(','):
                n = handle_num(n)
                f_out.write(str(n) + '\n')


if __name__ == "__main__":
    handle_article('org.dat', 'new_2009.txt')