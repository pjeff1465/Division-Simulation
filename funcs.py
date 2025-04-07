# Find bit position of q based on index 
# q = integer
def BitPosition(q, length):
    bin_str = format(q, f'0{length}b') # format binary string WITH leading zeros

    return bin_str[0] == '1' # check first element of string
# Returns true if index of q is 1, and false if 0

# Perform q = q + (-m)
# q, m = integer
# SubBinary works 
def SubBinary(q, m, length):
    # create mask so number length stay sames size and does not grow
    mask = (1 << length) - 1

    # 2's complement of m
    m_comp = ((~m) + 1) & mask

    result = q
    tmp_m = m_comp

    while tmp_m != 0:
        carry = result & tmp_m
        result = result ^ tmp_m
        tmp_m = carry << 1

    return result & mask

# Returns integer format of q - m

# Perform q = q + m ; Where q, m = integer
# Checked and works
def AddBinary(q, m, length):
    mask = (1 << length) - 1

    result = q
    tmp_m = m

    while tmp_m != 0:
        carry = result & tmp_m
        result = result ^ tmp_m
        tmp_m = carry << 1

    return result & mask
# Returns q = q + m

# Shift left AQ 
# Checked and works, return tuple
def ShiftLeft(a, q, length):
    combined = ((a << length) | q) << 1
    a = (combined >> length) & ((1 << length) - 1)
    q = combined & ((1 << length) - 1)
    
    return a, q

    ''' modified version, also works and also returns tuple
    mask = (1 << length) - 1

    combined = (a << length) | q

    combined = combined << 1

    new_a = (combined >> length) & mask
    new_q = combined & mask

    return new_a, new_q
    '''


def CheckOverflow(q, m, length):
    if(q == -2**(length-1)) & (m == -1):
        overflow = True
    else:
        overflow = False
