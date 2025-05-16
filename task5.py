def compute_prefix_function(s):
    n = len(s)
    pi = [0] * n
    for i in range(1, n):
        j = pi[i - 1]
        while j > 0 and s[i] != s[j]:
            j = pi[j - 1]
        if s[i] == s[j]:
            j += 1
        pi[i] = j
    return pi

# Зчитування вхідного рядка
s = input().strip()

# Обчислення довжини найбільшої грані
prefix_function = compute_prefix_function(s)
print(prefix_function[-1])