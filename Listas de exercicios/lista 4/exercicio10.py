N = int(input())

fibonacci = []

a, b = 0, 1
for i in range(N):
    fibonacci.append(a)
    a, b = b, a + b

print(" ".join(map(str, fibonacci)))
