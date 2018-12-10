# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s):
    ans = 0
    for c in s:
        ans = (ans * int(263) + ord(c)) % (100000000+3)
    return ans % (5*100000)

def _hash_key_func(c, input):
    ans = (input * int(263) + ord(c)) % (100000000+3)
    return ans % (5*100000)

def get_occurrences(pattern, text):
    result = []
    length = len(pattern)
    len_text = len(text)
    hash_key = _hash_func(pattern)
    hash_text = _hash_func(text[0:length])
    print('hash_key', hash_key, hash_text, pattern, text[0:length])
    if hash_text == hash_key and text[0:length] == pattern:
            result.append(length-1)
    for i in range(1, len_text - length + 1):
        hash_text = _hash_key_func(text[i], hash_text)
        print('hash_text', hash_text, text[i:i + length])
        if hash_text == hash_key and text[i:i + length] == pattern:
            result.append(i)
            print('find match:', i)
    return result
    #return [
    #    i 
    #    for ans = _hash_func(text[i:i + length], ans), i in range(len_text - length + 1)
    #    if ans == hash_key and text[i:i + length] == pattern
    #]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

