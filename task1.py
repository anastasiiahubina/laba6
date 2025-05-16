P = input().strip()
T = input().strip()

m = len(P)
n = len(T)

found = False

for i in range(n - m + 1):  # всі можливі підрядки T довжини m
    match = True
    for j in range(m - 1, -1, -1):  # справа наліво
        print(P[j], end='')  # вивід символу P[j]
        if T[i + j] != P[j]:
            match = False
            break
    if match:
        print()  # новий рядок після символів
        print(i + 1)  # позиція входження (зсув на 1)
        found = True
        break  # лише перше входження!
if not found:
    print()  # новий рядок після символів
    print(0)