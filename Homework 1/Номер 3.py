def zeros(n):
    answer = float('inf')
    primfac = [2, 5]
    for check_n in primfac:
        check = 0
        while n / check_n >= 1:
            check += int(n / check_n)
            check_n *= check_n
        answer = min(answer, check)
    return answer
