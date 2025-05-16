S = input().strip()
l, r = map(int, input().split())

substring = S[l - 1:r]
length = len(substring)

# Кількість префіксів = довжина + 1 (включає порожній)
print(length + 1)

# Власні префікси — від довжини 1 до (length - 1)
for i in range(1, length):
    print(substring[:i])