n = int(input())
word = [input() for _ in range(n)]
word.sort()
for c in word:
    print(c)