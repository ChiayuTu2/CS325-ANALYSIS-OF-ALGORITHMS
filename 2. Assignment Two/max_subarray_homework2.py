import sys
import timeit

# Usage when run from the command line: python max_subarray_homework2.py <filename>.
# Example usage:                        python max_subarray_homework2.py num_array_500.txt

def max_sub_s_d(A, s, n):
    if(s == n):
        return A[s]

    m = (s + n) // 2

    cur_val = 0
    lval = -10000

    for i in range(m, (s - 1), -1):
        cur_val += A[i]
        if (cur_val > lval):
            lval = cur_val
    
    cur_val = 0
    rval = -10000

    for i in range((m+1), (n + 1)):
        cur_val += A[i]
        if(cur_val>rval):
            rval = cur_val

    return max(max_sub_s_d(A, s, m), max_sub_s_d(A, (m + 1), n), max((lval + rval), lval, rval))

def max_subarray_simplification_delegation(A):
    """
    Computes the value of a maximum subarray of the input array by "simplification and delegation."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    return max_sub_s_d(A, 0, len(A)- 1)


#def max_subarray_simplification_delegation(A):
    """
    Computes the value of a maximum subarray of the input array by "simplification and delegation."
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """

    # TODO: Implement this function!
    # return None


def time_alg(alg, A):
    """
    Runs an algorithm for the maximum subarray problem on a test array and times how long it takes.
    
    Parameters:
        alg: An algorithm for the maximum subarray problem.
        A: A list (array) of n >= 1 integers.
    
    Returns:
        A pair consisting of the value of alg(A) and the time needed to execute alg(A) in seconds.
    """

    start_time = timeit.default_timer() # The start time in seconds.
    max_subarray_val = alg(A)
    end_time   = timeit.default_timer() # The end time in seconds.
    return max_subarray_val, end_time - start_time

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

for alg in [max_subarray_simplification_delegation]:
    print(file_name, time_alg(alg, A))