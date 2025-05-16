P = input().strip()
T = input().strip()

m = len(P)
n = len(T)

positions = []
comparison_count = 0

for i in range(n - m + 1):  # всі можливі підрядки T довжини m
    match = True
    for j in range(m - 1, -1, -1):  # справа наліво
        comparison_count += 1
        if T[i + j] != P[j]:
            match = False
            break
    if match:
        positions.append(str(i + 1))  # зсув на 1, бо позиції з 1

# Вивід:
# якщо входжень не було — перший рядок: 0
if positions:
    print(' '.join(positions))
else:
    print(0)

print(comparison_count)