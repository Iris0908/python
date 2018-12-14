# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * int(263) + ord(c)) % (100000000+3)
    return ans

def _hash_key_func(cur, pre, input, y):
    return (input*int(263) + ord(cur) - y*ord(pre)) % (100000000+3)

def get_occurrences(pattern, text):
    result = []
    length = len(pattern)
    len_text = len(text)
    hash_key = _hash_func(pattern)
    hash_text = _hash_func(text[len_text - length:len_text])
    #print('hash_key', hash_key, hash_text, pattern, text[len_text - length:len_text])
    if hash_text == hash_key and text[len_text - length:len_text] == pattern:
            result.append(len_text - length)
    y = 1
    for i in range(length):
        y = (y * int(263)) % (100000000+3)
    for i in range(len_text - length - 1, -1, -1):
        hash_text = _hash_key_func(text[i], text[i+length], hash_text, y)
        #print('hash_text', hash_text, text[i:i+length])
        if hash_text == hash_key and text[i:i+length] == pattern:
            result.append(i)
            #print('find match:', i)
    return reversed(result)
    #return [
    #    i 
    #    for ans = _hash_func(text[i:i + length], ans), i in range(len_text - length + 1)
    #    if ans == hash_key and text[i:i + length] == pattern
    #]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

