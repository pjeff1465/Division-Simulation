# Find bit position of a based on index 
def BitPosition(a, index):
    return(a & (1 << index)) != 0
# Returns true if index of a is 1, and false if 0

# Perform a = a + (-b)
def SubBinary(a, b):
    while b != 0:
        borrow = (~a) & b
        a = a ^ b
        b = borrow << 1
    return a
# Returns integer format of a - b 

