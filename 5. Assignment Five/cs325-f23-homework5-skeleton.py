import sys

def file_contents_letters(file_name):
    """
    Takes a file name as input and returns a string consisting of the file's contents
    with all non-letter characters removed.
    
    Parameters:
        file_name: The name of the file.
    
    Returns:
        A string with the contents of <file_name> but with all non-letter characters removed.
    """

    f = open(file_name, "r")
    file_contents = f.read()
    f.close()
    return "".join([c for c in file_contents if c.isalpha()])
    
def edit_distance(s1, s2, ci, cd, cm):
    """
    Computes the edit distance between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        ci: The cost of an insertion (1 by default).
        cd: The cost of a deletion (1 by default).
        cm: The cost of a mutation (1 by default).
    
    Returns:
        The edit distance between s1 and s2.
    """

    lenS1 = len(s1)
    lenS2 = len(s2)

    matrix = []

    for k in range(lenS1 + 1):
        row = [0] * (lenS2 + 1)
        matrix.append(row)

    for i in range(lenS1 + 1):
        matrix[i][0] = i * cd
    for j in range(lenS2 + 1):
        matrix[0][j] = j * ci

    for i in range(1, lenS1 + 1):
        for j in range(1, lenS2 + 1):
            if s1[i - 1] == s2[j - 1]:
                cost = 0
            else:
                cost = cm

            matrix[i][j] = min(
                matrix[i - 1][j] + cd,
                matrix[i][j - 1] + ci,
                matrix[i - 1][j - 1] + cost
            )

    # TODO: Implement this function!
    return matrix[lenS1][lenS2]
    
def lcs(s1, s2, output_sequence):
    """
    Computes the length of the longest common subsequence between two strings, s1 and s2.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        output_sequence: If set to "False" output the length of an LCS, if "True" output *some* LCS.
    
    Returns:
        The length of the longest common subsequence between s1 and s2.
    """

    lenS1 = len(s1)
    lenS2 = len(s2)

    matrix = []

    for k in range(lenS1 + 1):
        row = [0] * (lenS2 + 1)
        matrix.append(row)

    for i in range(1, lenS1 + 1):
        for j in range(1, lenS2 + 1):
            if s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1
            else:
                matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
    if not output_sequence:
        return matrix[lenS1][lenS2]
    
    lcsSeq = ""

    i = lenS1
    j = lenS2
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            lcsSeq = s1[i - 1] + lcsSeq
            i -= 1
            j -= 1
        elif matrix[i - 1][j] > matrix[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # TODO: Implement this function!
    return lcsSeq
    
def lcs3(s1, s2, s3):
    """
    Computes the length of the longest common subsequence between three strings: s1, s2, and s3.
    
    Parameters:
        s1: The first string.
        s2: The second string.
        s3: The third string.
    
    Returns:
        The length of the longest common subsequence between s1, s2, and s3.
    """

    lenS1 = len(s1)
    lenS2 = len(s2)
    lenS3 = len(s3)

    matrix = []

    for _ in range(lenS1 + 1):
        layer = []
        
        for _ in range(lenS2 + 1):
            row = [0] * (lenS3 + 1)
            layer.append(row)
        
        matrix.append(layer)


    for i in range(1, lenS1 + 1):
        for j in range(1, lenS2 + 1):
            for k in range(1, lenS3 + 1):
                if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                    matrix[i][j][k] = matrix[i - 1][j - 1][k - 1] + 1
                else:
                    matrix[i][j][k] = max(matrix[i - 1][j][k], matrix[i][j - 1][k], matrix[i][j][k - 1])

    return matrix[lenS1][lenS2][lenS3]

    # TODO: Implement this function!
    return None


s1 = file_contents_letters('COVID-RefDec19.txt')
s2 = file_contents_letters('COVID-OmicronBA1.txt')
# print(edit_distance(s1, s2, 1, 1, 1))
S1 = 'AGGCA'
S2 = 'CTTGA'
S3 = 'GTA'

test1 = 'BURRITO'
test2 = 'ERROR'

print('When S1 is AGGCA and S2 is CTTGA, the LCS is:', lcs(S1, S2, False))
print(lcs(S1, S2, True))
print(lcs3(S1, S2, S3))

print('When S1 is BURRITO and S2 is ERROR, the LCS is:', lcs(test1, test2, False))
print(lcs(test1, test2, True))



