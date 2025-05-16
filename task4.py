def find_substring_occurrences(a: str, b: str):
    positions = []
    for i in range(len(a) - len(b) + 1):
        if a[i:i + len(b)] == b:
            positions.append(i + 1)  # +1 бо індексація з 1
    print(len(positions))
    if positions:
        print(' '.join(map(str, positions)))

# Зчитування вхідних даних
a = input().strip()
b = input().strip()

find_substring_occurrences(a, b)