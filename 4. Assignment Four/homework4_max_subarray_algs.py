import sys
import timeit

# Usage when run from the command line: python max_subarray_algs.py <filename>.
# Example usage:                        python max_subarray_algs.py num_array_10000.txt

file_name = sys.argv[1]

f = open(file_name, "r")
A = [int(num) for num in f.readline().strip().split(" ")]
f.close()

def max_subarray_recursion_inversion(A):
    """
    Computes the value of a maximum subarray of the input array by "recursion inversion" (i.e., dynamic programming).
    
    Parameters:
        A: A list (array) of n >= 1 integers.
    
    Returns:
        The sum of the elements in a maximum subarray of A.
    """
    n = len(A)
    cur_val = 0
    max_val = -10000
    for i in range(0, n):
        cur_val+=A[i]
        if(cur_val < 0):
            cur_val = 0
        elif(max_val < cur_val):
            max_val = cur_val
    return max_val
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

for alg in [max_subarray_recursion_inversion]:
    print(file_name, time_alg(alg, A))