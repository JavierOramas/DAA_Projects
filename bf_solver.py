def check_prefix(T, A):
    return len(A) >= len(T) and T == A[0: len(T)]

def bf_solution(T, S):
    count = [0]
    permutations = []

    def inner(s, a, s_index, permutation):
        if len(s) == 0:
            if check_prefix(T, a):
                count[0] += 1
                permutations.append((a, permutation))
        else:
            inner(s[1:], f'{s[0]}{a}', s_index + 1, [s_index, *permutation])
            inner(s[1:], f'{a}{s[0]}', s_index + 1, [*permutation, s_index])
    
    inner(S[1:], S[0], 1, [0])

    return count[0]