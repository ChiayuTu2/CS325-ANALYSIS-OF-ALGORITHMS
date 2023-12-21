import numpy as np
from sys import argv

# Usage (run from the command line): python chomping_logs.py <file_containing_V_data> <LF> <LM>

"""
Examples:
python chomping_logs.py test22.txt 2 2
20
python chomping_logs.py test22.txt 2 0
6
python chomping_logs.py test22.txt 0 2
10
"""

"""
Computes the maximum amount of revenue achievable by chomping a fir log of length LF and maple log of length LM into bundles,
with prices according to V.

Parameters:
    V: The log bundle value input matrix.
    LF: The length of the input fir log.
    LM: The lenfth of the input maple log.

Returns:
    The maximum amount of revenue achievable by chomping a fir log of length LF and maple log of length LM into bundles.
"""
def log_values(V, LF, LM):
    # TODO: Implement this function and set its return value correctly!
    # Hint: The command np.zeroes((x, y), "int") returns an x-by-y matrix initialized to all zeroes.

    matrix = []
    for i in range(LF + 1):
        matrix.append([0] * (LM + 1))

    if LM == 0:
        max_value = 0
        for i in range(LF + 1):
            max_value = max(max_value, V[i][0])
        return max_value

    for i in range(1, LF + 1):
        for j in range(1, LM + 1):
            for k in range(i + 1):
                for u in range(j + 1):
                    if k <= i and u <= j:
                        matrix[i][j] = max(matrix[i][j], matrix[i - k][j - u] + V[k][u])

    return matrix[LF][LM]

def read_V_from_file(file_name):
    VL = []
    f = open(file_name, "r")
    for line in f:
        VL += [[int(num) for num in line.strip().split()]]
    f.close()
    return np.array(VL)

file_name = argv[1]
V = read_V_from_file(file_name)
LF = int(argv[2])
LM = int(argv[3])

# Uncomment the following line to check how the input matrix V was parsed.
# print(V)

print(log_values(V, LF, LM))