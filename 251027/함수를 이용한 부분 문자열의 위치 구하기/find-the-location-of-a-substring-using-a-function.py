text = input()
pattern = input()

# Please write your code here.
def f(text, pattern):
    for t in range(len(text)):
        l = len(pattern)
        if text[t:t+l] == pattern:
            return t
    return -1

print(f(text, pattern))