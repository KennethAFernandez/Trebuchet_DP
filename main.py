import sys
import time

REC_COUNT = 0
DP_COUNT = 0

def rec(p_val, t_val):

    # Initialize counter
    global REC_COUNT
    REC_COUNT += 1

    # Check base cases
    if (t_val == 0): return 0
    if (t_val == 1): return 1
    if (p_val == 1): return t_val

    max_vals = []
    for i in range(1, t_val):
        max_vals.append(1 + max(rec(p_val - 1, i - 1), rec(p_val, t_val - i)))
    
    return min(max_vals)


def dp(p_val, t_val):

    # Initialize Counter
    global DP_COUNT
    DP_COUNT += 1

    # Check base cases
    if (mtx[p_val - 1][t_val - 1] != -1):
        return mtx[p_val - 1][t_val - 1]

    if (t_val == 0): 
        mtx[p_val - 1][t_val - 1] = 0
        return 0

    if (t_val == 1): 
        mtx[p_val - 1][t_val - 1] = 1
        return 1

    if (p_val == 1): 
        mtx[p_val - 1][t_val - 1] = t
        return t_val


    # Recurrence Relation
    max_vals = []
    for i in range(1, t_val + 1):
        max_vals.append(1 + max(dp(p_val - 1, i - 1), dp(p_val, t_val - i)))

    # Set value in matrix
    mtx[p_val - 1][t_val - 1] = min(max_vals)

    # Return min val.
    return min(max_vals)


if __name__ == '__main__':

    print('\n===============================')
    print('Start of program! (Trebuchet)')
    sys.setrecursionlimit(3000)
    # Initialize vars. & create matrix
    start = time.time()
    p = int(sys.argv[1])
    t = int(sys.argv[2])
    mtx = [[-1 for j in range(t + 1)] for i in range(p)]

    # Call algo.
    for i in range(1, t):
        for j in range(1, p):
            mtx[j - 1][i - 1] = dp(j, i)   
    
    # Print generated sol.
    print('===============================')
    print(f'Num. of Pumpkins  =>  [{p}]')
    print(f'Num. of Targets   =>  [{t}]')
    print('===============================')
    print(f'Num. Calls DP     =>  [{DP_COUNT}]')
    print(f'D.P. Solution     =>  [{dp(p, t)}]')
    # print('===============================')
    # print(f'Num. Calls Rec.   =>  [{REC_COUNT}]')
    # print(f'Rec. Solution     =>  [{rec(p, t)}]')
    print('===============================')
    print(f'Time: {time.time() - start}\n')

    