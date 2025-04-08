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

# Checks overflow, overflow occurs when allocated bit length is not big enough to hold quotient
def CheckOverflow(q, m, length):
    max_val = 2**(length-1) - 1
    return ((q == -2**(length-1)) and (m == -1)) or abs(q) > max_val or abs(m) > max_val
# returns true if overflow occurs, and false if not

# convert binary string to SIGNED integer
def binary_to_int(bin_str):
    if bin_str[0] == '0': # binary is positive
        return int(bin_str, 2) # convert it like normal
    else: # negative, first bit negated take int of binary numbers
        new_str = bin_str[1:] # dismiss sign bit
        bits = len(new_str) 
        value = int(new_str, 2)
        return -value # return negative of value

# Needed to convert integer to SIGNED magnitude
def int_to_binary(num, length):
    if num >= 0:
        return format(num, f'0{length}b'.zfill(length))
    else:
        magnitude = abs(num)
        binary = format(magnitude, f'0{length-1}b').zfill(length-1)
        return '1' + binary
    
# function used to print restore results table
def PrintRestore(RestoreResults):
    print("\n=== Restoring Division Results ===")
    print("-" * 146)
    print("| {:<4} | {:<26} | {:<14} | {:<35} | {:<34} | {:<5} | {:<7} |".format(
        "No.", "Dividend", "Divisor", "Quotient (Bin/Hex)", "Remainder", "Iter", "Add/Sub"))
    print("-" * 146)

    for i, result in enumerate(RestoreResults):
        print("| {:<4} | {:<26} | {:<14} | {:<35} | {:<34} | {:<5} | {:<7} |".format(
            i+1,
            result["Operand 1"],
            result["Operand 2"],
            f"{result['Quotient']['Binary']} ({result['Quotient']['Hex']})",
            f"{result['Remainder']['Binary']} ({result['Remainder']['Hex']})",
            result["Number of iterations"],
            result["Number of Additions/Subtractions"]
        ))
    print("-" * 146)
    return

# function used to print NonRestore results
def PrintNonRestore(NonRestoreResults):
    print("\n=== Non-Restoring Division Results ===")
    print("-" * 146)
    print("| {:<4} | {:<26} | {:<14} | {:<35} | {:<34} | {:<5} | {:<7} |".format(
        "No.", "Dividend", "Divisor", "Quotient (Bin/Hex)", "Remainder", "Iter", "Add/Sub"))
    print("-" * 146)
    
    for i, result in enumerate(NonRestoreResults):
        print("| {:<4} | {:<26} | {:<14} | {:<35} | {:<34} | {:<5} | {:<7} |".format(
            i+1,
            result["Operand 1"],
            result["Operand 2"],
            f"{result['Quotient']['Binary']} ({result['Quotient']['Hex']})",
            f"{result['Remainder']['Binary']} ({result['Remainder']['Hex']})",
            result["Number of iterations"],
            result["Number of Additions/Subtractions"]
        ))
    print("-" * 146)
    return 

def PrintResults(NonRestoreResults, RestoreResults):
    