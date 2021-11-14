import sys
import time

REC_COUNT = 0
DP_COUNT = 0

# Recursive algorithm to solve the Trebuchet problem
def rec(p_val, t_val):

    # Global var. counter that keeps track of the amount of times that 
    # the recursive function has been called
    global REC_COUNT
    REC_COUNT += 1
    max_vals = []

    # Check base cases 
    if t_val == 0 or t_val == 1: return t_val
    if p_val == 1: return t_val

    # Just iterate through determing which of the sub-problem sols. to add
    for i in range(1, t_val):
        max_vals.append(1 + max(rec(p_val - 1, i - 1), rec(p_val, t_val - i)))

    return min(max_vals)


def dp(p_val, t_val):
    global DP_COUNT
    DP_COUNT += 1
    max_vals = []
    
    # If pumpkin exploded return the corresponding value from the mtx.
    if (mtx[p_val - 1][t_val - 1] != -1):
        return mtx[p_val - 1][t_val - 1]

    # Check base cases: T(p, 0), T(p, 1) & T(1, t) - just return t_val
    if t_val == 0 or t_val == 1 or p_val == 1:
        mtx[p_val - 1][t_val - 1] = t_val
        return t_val 

    # Break down into two sub-problems (p-1 & x-1) or (p & t-x)
    # Take maximum of two sub-problems since we are finding min.
    # number of throws in the worst case. Then store the one that 
    # minimizes the maximum number of throws
    for i in range(1, t_val + 1):
        to_add =  max(dp(p_val - 1, i - 1), dp(p_val, t_val - i))
        max_vals.append(1 + to_add)
    # Store values in DP table
    mtx[p_val - 1][t_val - 1] = min(max_vals)

    # Store list in traceback table for the tracback step
    tb_mtx[p_val - 1][t_val - 1] = max_vals
    return min(max_vals)


def traceback(p_val, t_val, off_val, mtx, tb_mtx, targs):

    # Check base cases
    if p_val == 1 or t_val == 1 or t_val == 0:
        targs.append(off_val + 1)
        # print(f'(Base) Targets:         {targs} ')
        return

    # If there are multiple targets that can be attempted, chooses the target that is closest
    # Assigns the next target to the var. & append target
    # print(f'Traceback:  {tb_mtx[p_val -1][t_val -1]}')
    # print(f'Min:        {min(tb_mtx[p_val - 1][t_val - 1])}')
    # print(f'Index:      {tb_mtx[p_val - 1][t_val - 1].index(min(tb_mtx[p_val - 1][t_val - 1]))}')
    
    val_idx = tb_mtx[p_val - 1][t_val - 1]
    temp = val_idx.index(min(tb_mtx[p_val - 1][t_val - 1])) 
    next_targ = temp + 1
    targs.append(off_val + next_targ)

    # print(f'Next Targ:  {next_targ}')
    # print(f'Targets:    {targs}')
    # print('\n')
    
    # Recursive calls if worst case happens / increment offset value in else
    if (mtx[p_val - 1][t_val - next_targ - 1]) < (mtx[p_val - 2][next_targ - 2]):
        traceback(p_val - 1, next_targ - 1, off_val, mtx, tb_mtx, targs)

    else:
        traceback(p_val, t_val - next_targ, next_targ + off_val, mtx, tb_mtx, targs)



if __name__ == '__main__':
    start = time.time()
    sys.setrecursionlimit(3000)

    p = int(sys.argv[1])
    t = int(sys.argv[2])
    targs_attempted = []

    mtx = [[-1 for j in range(t + 1)] for i in range(p)]
    tb_mtx = [[-1 for j in range(t + 1)] for i in range(p)]

    for i in range(1, p):
        for j in range(1, t):
            mtx[i - 1][j - 1] = dp(i, j)   

    sol = dp(p, t)
    traceback(p, t, 0, mtx, tb_mtx, targs_attempted)
    print(sol)
    print(str(' '.join(map(str, targs_attempted))))

    # Print calculated solutions
    # T(p, t) represents the min. number of throws necessary in the worst
    # case to find the max. length when given p & t
    # print('\n===============================')
    # print('Start of program! (Trebuchet)')
    # print('===============================')
    # print(f'Num. of Pumpkins  =>  [{p}]')
    # print(f'Num. of Targets   =>  [{t}]')
    # print('===============================')
    # print(f'Num. Calls DP     =>  [{DP_COUNT}]')
    # print(f'D.P. Solution     =>  [{dp(p, t)}]')
    # print('===============================')
    # print(f'Rec. Solution     =>  [{rec(p, t)}]')
    # print(f'Num. Calls Rec.   =>  [{REC_COUNT}]')
    # print('===============================')
    # print(f'Time: {time.time() - start}\n')
    # print('\n')
    # for i in targs_attempted:
    #     print(f'{i}')
    # print('\n')

    # Need this to run the recursive algo with larger inputs
    # Start timer to calc. runtime of dp/rec. algos.

    # Initialize Counter to keep track of amount of calls to this func.
    # Make sure this the correct count & includes the initial call

    # If the targets num. is zero or one, return the target value
    # If the pumpkin num. is one, return the target value

    
    # Set value in matrix - keeping track of calculated values
    # to avoid recomputation
    # Return minimum val. that maxmizes number of throws

    # global variables used as counters for the recursive 
    # and Dynamic Progamming algorithms