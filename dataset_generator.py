from bf_solver import bf_solution
import random
import string

def gen():
    flag = False

    while not flag:
        min_len = 5

        st_len = random.randint( min_len, 2*min_len)
        in_dat = ''.join(random.choice(string.ascii_lowercase) for i in range(st_len))

        min_len += 1

        max_pat_len = max(4,int(min_len/2))
        
        pat_len = random.randint(3,max_pat_len)
        pat_dat = ''.join(random.choice(string.ascii_lowercase) for i in range(pat_len))
        
        count_ways = bf_solution(pat_dat, in_dat)

        if count_ways > 0:
            flag = True
        
    return (pat_dat, in_dat), count_ways
    




            

