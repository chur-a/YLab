def count_find_num(primesL, limit):
    max_number = counter = 0
    visited = set()

    def dfs(primesL):
        nonlocal counter, max_number
        number = 1
        for n in primesL:
            number *= n
        if number > limit or number in visited:
            return
        else:
            counter += 1
            visited.add(number)
            max_number = max(number, max_number)
            for n in primesL:
                dfs(primesL + [n])
    
    dfs(primesL)
    return [counter, max_number] if counter else []
