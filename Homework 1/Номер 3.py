def zeros(n):
    zeros_n = 0
    while n // 5 != 0:
        zeros_n = zeros_n + n // 5
        n = n // 5
    return zeros_n

