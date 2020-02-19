def is_the(word: str):
    word = word.lower()
    return word == 'the'


def handle_word(word: str):
    s = ''
    for c in word:
        if c.isalnum():
            s += c
    return s[:1].upper() + s[1:]


def handle_article(path_from, path_to):
    with open(path_from, 'r') as f_in:
        with open(path_to, 'w') as f_out:
            for w in f_in.read().split():
                if is_the(w):
                    continue
                w = handle_word(w)
                f_out.write(w + '\n')


if __name__ == "__main__":
    handle_article('test.txt', 'new_2008.txt')
