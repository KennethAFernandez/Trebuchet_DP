import sys
import time


# global variables used as counters for the recursive 
# and Dynamic Progamming algorithms
REC_COUNT = 0
DP_COUNT = 0


# Recursive algorithm to solve the problem & also counts
# the amount of calls made by the program to the func.
def rec(p_val, t_val):

    # Initialize counter
    global REC_COUNT
    REC_COUNT += 1

    # Check base cases
    if t_val == 0 or t_val == 1: return t_val
    if p_val == 1:               return t_val

    # xth target i sone that lies between 1 & t inclusive
    # Two sub-problems: (p-1 & x-1) or (p & t-x)
    # Take maximum of two sub-problems
    max_vals = []
    for i in range(1, t_val):
        max_vals.append(1 + max(rec(p_val - 1, i - 1), rec(p_val, t_val - i)))

    # Pick the one that minimizes the max. number of throws
    return min(max_vals)

# Dynamic Programming Algorithm that uses a matrix to 
# avoid recomputataion to compute the minimum number 
# of throws necessary
def dp(p_val, t_val):

    # Initialize Counter to keep track of amount of calls to this func.
    # Make sure this the correct count & includes the initial call
    global DP_COUNT
    DP_COUNT += 1

    # If pumpkin exploded return the corresponding value from the mtx.
    # Check base cases: T(p, 0), T(p, 1) & T(1, t)
    # If the targets num. is zero or one, return the target value
    # If the pumpkin num. is one, return the target value
    if (mtx[p_val - 1][t_val - 1] != -1):
        return mtx[p_val - 1][t_val - 1]
    
    if t_val == 0 or t_val == 1:
        mtx[p_val - 1][t_val - 1] = t_val
        return t_val 

    if (p_val == 1): 
        mtx[p_val - 1][t_val - 1] = t_val
        return t_val

    # Recurrence Relation
    # Break down into two sub-problems (p-1 & x-1) or (p & t-x)
    # Take maximum of two sub-problems since we are finding min.
    # number of throws in the worst case. Then store the one that 
    # minimizes the maximum number of throws (line 61)
    max_vals = []
    for i in range(1, t_val + 1):
        max_vals.append(1 + max(dp(p_val - 1, i - 1), dp(p_val, t_val - i)))
    
    # Set value in matrix - keeping track of calculated values
    # to avoid recomputation
    mtx[p_val - 1][t_val - 1] = min(max_vals)

    # Return minimum val. that maxmizes number of throws
    return min(max_vals)

# IMPLEMENT TRACEBACK STEP
def traceback():
    print('')



if __name__ == '__main__':

    print('\n===============================')
    print('Start of program! (Trebuchet)')

    # Need this to run the recursive algo with larger inputs
    sys.setrecursionlimit(3000)


    # Initialize vars. & create matrix
    p = int(sys.argv[1])
    t = int(sys.argv[2])
    start = time.time()
    mtx = [[-1 for j in range(t + 1)] for i in range(p)]

    # Call algo.
    for i in range(1, t):
        for j in range(1, p):
            mtx[j - 1][i - 1] = dp(j, i)   
    
    # for i in mtx:
    #     print(i)
    # T(p, t) represents the min. number of throws necessary in the worst
    # case to find the max. length when given p & t
    print('===============================')
    print(f'Num. of Pumpkins  =>  [{p}]')
    print(f'Num. of Targets   =>  [{t}]')
    print('===============================')
    print(f'Num. Calls DP     =>  [{DP_COUNT}]')
    print(f'D.P. Solution     =>  [{dp(p, t)}]')
    print('===============================')
    print(f'Rec. Solution     =>  [{rec(p, t)}]')
    print(f'Num. Calls Rec.   =>  [{REC_COUNT}]')
    print('===============================')
    print(f'Time: {time.time() - start}\n')

    