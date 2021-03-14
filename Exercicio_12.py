x = range(1,6)
n = 0
print()
for c in x:
    n += 1
    p = "*" * n
    print(p)
for c in x:
    n -= 1
    p = "*" * n
    print(p)