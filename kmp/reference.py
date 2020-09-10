# Python program for KMP Algorithm
def KMPSearch(pat, txt):
    """
    time complexity of big-omega(T) (iterate through text once tgt with pattern)
    """
    P = len(pat)
    T = len(txt)

    # create lps[] that will hold the longest prefix suffix
    # values for pattern
    lps = [0]*P
    j = 0 # index for pat[]

    # Preprocess the pattern (calculate lps[] array)
    computeLPSArray(pat, P, lps)
    print(lps)

    i = 0 # index for txt[]
    while i < T:
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == P:
            print("Found pattern at index " + str(i-j))
            j = lps[j-1]

        # mismatch after j matches
        elif i < T and pat[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

def computeLPSArray(pat, P, lps):
    """
    time complexity of big-omega(P) (iterate through pattern of size P to get lps table)
    space complexity of big-omega(P) (store lps table of size P)
    """
    length = 0 # length of the previous longest prefix suffix

    lps[0] # lps[0] is always 0
    i = 1

    # the loop calculates lps[i] for i = 1 to P-1
    while i < P:
        if pat[length]== pat[i]:
                length += 1
                lps[i] = length
                i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length-1]

            # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

# txt = "ABABDABACDABABCABAB"
# pat = "ABABCABAB"
txt = "abcdfaf"
pat = "abcdghgdhabc"
KMPSearch(pat, txt)

# This code is contributed by Bhavya Jain

