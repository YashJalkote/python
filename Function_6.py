def natural(n):
    if n == 0:
        return 0
    else:
        return n + natural(n - 1)

print("Sum =", natural(5))