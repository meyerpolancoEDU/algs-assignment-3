import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def med_top_down(S, T, MED={}):
    ## look up the memory
    if (S, T) in MED:
        return MED[(S, T)]
    ## base cases
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    ## recursive cases
    if S[0] == T[0]:  # If first characters are the same, move to the next
        MED[(S, T)] = med_top_down(S[1:], T[1:], MED)
    else:
        insert = med_top_down(S, T[1:], MED) + 1  # Insert a character
        delete = med_top_down(S[1:], T, MED) + 1  # Delete a character
        MED[(S, T)] = min(insert, delete)
    
    return MED[(S, T)]
    
def fast_MED(S, T):
    '''Bottom-up memoization implementation of MED'''
    m = len(S)
    n = len(T)
    
    # Create a table to store edit distances
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Base cases: filling first row and column
    # table[0][j] = j
    for j in range(n + 1):
        table[0][j] = j
    
    # table[i][0] = i
    for i in range(m + 1):
        table[i][0] = i
    
    # Fill the table bottom-up
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] == T[j-1]:
                # Characters match, no cost
                table[i][j] = table[i-1][j-1]
            else:
                # Characters don't match, choose minimum of insert or delete
                insert = table[i][j-1] + 1  # Insert character from T
                delete = table[i-1][j] + 1  # Delete character from S
                table[i][j] = min(insert, delete)

    return table[m][n]

def align_helper(S, T):
    """Helper function, same as fast_MED but returns the table instead of the edit distance"""
    m = len(S)
    n = len(T)
    
    table = [[0] * (n + 1) for _ in range(m + 1)]
    
    for j in range(n + 1):
        table[0][j] = j
    
    for i in range(m + 1):
        table[i][0] = i
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if S[i-1] == T[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                insert = table[i][j-1] + 1  # Insert character from T
                delete = table[i-1][j] + 1  # Delete character from S
                table[i][j] = min(insert, delete)

    return table
    

def fast_align_MED(S, T):
    '''Returns aligned versions of S and T showing the edit operations'''
    # Get the DP table using the helper function
    table = align_helper(S, T)
    
    m = len(S)
    n = len(T)
    
    # Traceback from table[m][n] to reconstruct the alignment
    align_S = []
    align_T = []
    i, j = m, n
    
    while i > 0 or j > 0:
        if i > 0 and j > 0 and S[i-1] == T[j-1]:
            # Characters match, align them
            align_S.append(S[i-1])
            align_T.append(T[j-1])
            i -= 1
            j -= 1
        elif i > 0 and j > 0:
            # Characters don't match, check which operation to use
            if table[i][j] == table[i-1][j] + 1:
                # Delete from S (gap in T)
                align_S.append(S[i-1])
                align_T.append('-')
                i -= 1
            else:
                # Insert from T (gap in S)
                align_S.append('-')
                align_T.append(T[j-1])
                j -= 1
        elif j > 0:
            # Only T has remaining characters - insert them
            align_S.append('-')
            align_T.append(T[j-1])
            j -= 1
        else:  # i > 0
            # Only S has remaining characters - delete them
            align_S.append(S[i-1])
            align_T.append('-')
            i -= 1
    
    # Reverse since we built the alignment backwards
    align_S.reverse()
    align_T.reverse()
    
    return (''.join(align_S), ''.join(align_T))

print(fast_align_MED("kookaburra", "kookybird"))