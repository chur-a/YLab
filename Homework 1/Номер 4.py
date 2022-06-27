from itertools import combinations


def bananas(s) -> set:
    result = set()
    check = 'banana'
    t = len(s) - len(check)
    for inst in combinations((_ for _ in range(len(s))), t):
        a = list(s)
        for i in inst:
            a[i] = '-'
        a = ''.join(a)
        if check == a.replace('-', ''):
            result.add(a)
    return result

