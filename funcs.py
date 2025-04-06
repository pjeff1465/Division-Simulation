# Find bit position of q based on index 
# q = integer
def BitPosition(q, length):
    bin_str = format(q, f'0{length}b') # format binary string WITH leading zeros

    return bin_str[0] == '1' # check first element of string
# Returns true if index of q is 1, and false if 0

# Perform q = q + (-m)
# q, m = integer
def SubBinary(q, m):
    while m != 0:
        carry = (~q) & m
        q = q ^ m
        m = carry << 1
    return q
# Returns integer format of q - m

# Perform q = q + m ; Where q, m = integer
def AddBinary(q, m):
    while m != 0:
        carry = q & m
        q = q ^ m
        m = carry << 1
    return q 
# Returns q = q + m