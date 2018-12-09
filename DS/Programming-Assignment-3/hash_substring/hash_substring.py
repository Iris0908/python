# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def _hash_func(s):
    ans = 0
    for c in reversed(s):
        ans = (ans * self._multiplier + ord(c)) % self._prime
    return ans % self.bucket_count

def get_occurrences(pattern, text):
    t = text.reversed()
    hash_key = _hash_func(pattern)
    return [
        i 
        for i in range(len(text) - len(pattern) + 1) 
        if _hash_func(t[i:i + len(pattern)]) == hash_key and text[i:i + len(pattern)] == pattern
    ]

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

