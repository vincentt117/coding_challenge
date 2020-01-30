# https://app.codesignal.com/challenge/KkRXXEt9DwaHFYk2K

def isCryptSolution(crypt, solution):
    # Build diciontary
    char_int_map = {}
    for i in solution:
        char_int_map[i[0]] = int(i[1])
    
    n_map = {0:0, 1:0, 2:0}
    for w_idx in range(len(crypt)):
        if char_int_map[crypt[w_idx][0]] == 0 and len(crypt[w_idx]) != 1:
            return False
        for c_idx in range(len(crypt[w_idx])):
            n_map[w_idx] += (char_int_map[crypt[w_idx][c_idx]] * (10 ** (len(crypt[w_idx]) - c_idx)))
    
    return n_map[0] + n_map[1] == n_map[2]
            

