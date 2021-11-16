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

    # Initalize vars. 
    global DP_COUNT
    DP_COUNT += 1
    max_vals = []
    temp = t_val
    
    # Break down into two sub-problems (p-1 & x-1) or (p & t-x)
    # Take maximum of two sub-problems since we are finding min.
    # number of throws in the worst case. Then store the one that 
    # minimizes the maximum number of throws
    for i in range(1, t_val + 1):

        # to_add = 1 + max(mtx[p_val - 1][i - 1], mtx[p_val][t_val - i])
        # Set values for the two sub problems so we can compare them
        exploded = mtx[p_val - 1][i - 1]
        survived = mtx[p_val][t_val - i]
        to_add = max(exploded, survived)

        # Determine if the pumpkin exploded or not
        # if pumpking exploded, append negative value, if the pumpkin
        # survived we just add the index to the TB table
        if to_add < temp:
            temp = to_add
            if exploded >= survived:
                # tb_vals.append(i * -1)
                tb_mtx[p_val][t_val] = i * -1
            else:
                # tb_vals.append(i)
                tb_mtx[p_val][t_val] = i

        max_vals.append(1 + to_add)

    # Set the value in the array
    mtx[p_val][t_val] = min(max_vals)
    # Return min 
    return min(max_vals)

def traceback(p_val, t_val, off_val):

    val_idx = tb_mtx[p_val][t_val]
    if val_idx < 0:
        targ = val_idx * -1
    else:
        targ = val_idx

    # If the target value drops below 1, we can return because there
    # is nothing left to do. The targets attempted array should be filled
    if t_val <= 0:
        return

    # If the value in the TB table is less than 0, we append a negative 
    # value plus the offset value
    if val_idx < 0:
        targs_attempted.append(-(targ + off_val))
    else:
        targs_attempted.append(targ + off_val)

    # If the value in the TB table is greater than 0, we can increment
    # the offset value by the absolute value of the table's value
    if val_idx > 0: 
        off_val += targ

    # Recursion 
    if tb_mtx[p_val][t_val] < 0 and p_val > 1:
        traceback(p_val - 1, t_val - (t_val - targ + 1), off_val)
    else:
        traceback(p_val, t_val - targ, off_val)


if __name__ == '__main__':
    start = time.time()
    sys.setrecursionlimit(3000)

    p = int(sys.argv[1])
    t = int(sys.argv[2])
    targs_attempted = []

    # Create matrices
    mtx = [[0 for j in range(t + 1)] for i in range(p)]
    tb_mtx = [[0 for j in range(t + 1)] for i in range(p)]

    # Deal with the base cases
    for i in range(1, t + 1):
        mtx[0][i] = i
        
    for i in range(1, p):
        mtx[i][1] = 1
        
    for i in range(2, t + 1):
        tb_mtx[0][i] = 1
        
    for i in range(0, p):
        tb_mtx[i][1] = -1

    # Call DP algorithm
    for i in range(1, p):
        for j in range(2, t + 1):
            mtx[i][j] = dp(i, j)   

    # Print solution
    sol = mtx[p - 1][t]
    traceback(p - 1, t, 0)
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
  