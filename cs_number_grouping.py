# https://app.codesignal.com/challenge/J785w3Xu4BFzqnREg

def numbersGrouping(a):
    count = 0
    seen_group = set()
    a.sort()
    a_idx = 0
    i = 1
    while a_idx < len(a):
        while a_idx < len(a) and (i - 1) * (10**4) + 1 <= a[a_idx] <= i * (10**4):
            if i not in seen_group:
                count += 1
                seen_group.add(i)
            a_idx += 1
            count += 1
        i += 1
    return count