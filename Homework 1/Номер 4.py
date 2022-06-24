from itertools import combinations


def bananas(s) -> set:
    result = set()
    check = 'banana'
    t = len(s) - len(check)
    A = list(combinations((_ for _ in range(len(s))), t))
    for inst in A:
        inst = set(inst)
        tmp_st = ''
        for i in range(len(s)):
            if i in inst:
                tmp_st += '-'
            else:
                tmp_st += s[i]
        if check == tmp_st.translate({ord('-'): None}):
            result.add(tmp_st)
    return result
