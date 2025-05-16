def z_to_prefix_function(z):
    n = len(z)
    p = [0] * n
    for i in range(1, n):
        for j in range(z[i]):
            if p[i + j] == 0:
                p[i + j] = j + 1
            else:
                break
    return p

# Зчитування вхідних даних
n = int(input())
z = list(map(int, input().split()))

# Обчислення префікс-функції
prefix = z_to_prefix_function(z)

# Вивід результату
print(' '.join(map(str, prefix)))