from funcs import *

# q_int, m_int ==> Magnitudes (sign bit negated)
def Restoring(q_int, m_int, q_sign, m_sign, length):    
    i = 0 #iterations
    n = length #Number of bits in q
    addSub = 0 #Number of Additions and Subtractions
    a = 0 # a = length of q
    q = q_int

    # works here
    #print(n)
    
    # Check Overflow
    if(CheckOverflow(q_int, m_int, length)): # overflow has occured!
        return {
            "Quotient": {"Binary": "Error Overflow!", "Hex": "Error"},
            "Remainder": {"Binary": "Error", "Hex": "Error"},
            "Number of iterations": "Error",
            "Number of Additions/Subtractions": "Error"
        }

    # Check if divisor is 0
      # Check if divisor is 0 
    if m_int == 0:
        return {
            "Quotient": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
            "Remainder": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
            "Number of iterations": "Error",
            "Number of Additions/Subtractions": "Error"
        }   
    
    # Enter Restore Algorithm
    while i < n:
        # Works here

        a, q = ShiftLeft(a, q, length) # perform SHL on AQ

        a = SubBinary(a, m_int, length)
        addSub += 1
                
        if BitPosition(a, length): # If A = negative
            q = q & ~1 # clear LSB in q

            # restore a ( a <- a + m )
            a = AddBinary(a, m_int, length)
            addSub += 1 # add operation so + 1

        else: # A is positive
            q = q | 1

        i += 1 # + 1 for number of iterations

    # final values determined from loop
    final_q = q
    final_a = a

    # determine correct sign of quotient and remainder
    quotient_sign = 0 if (q_sign == m_sign) else 1
    remainder_sign = q_sign


    # Take signed binary format of quotient (q) and remainder (a)
    q_bin = f"{quotient_sign}{format(abs(final_q), f'0{length - 1}b')}"
    a_bin = f"{remainder_sign}{format(abs(final_a), f'0{length - 1}b')}"

    finalq_int = binary_to_int(q_bin)
    finala_int = binary_to_int(a_bin)

    # Take signed hex format of quotient (q) and remainder (a)
    q_hex = hex(abs(finalq_int)) if finalq_int >= 0 else '-' + hex(abs(finalq_int))[2:]
    a_hex = hex(abs(finala_int)) if finala_int >= 0 else '-' + hex(abs(finala_int))[2:]

    # Store everything in a dictionary
    RestoreResults = {"Quotient": {"Binary": q_bin, "Hex": q_hex},
                      "Remainder": {"Binary": a_bin, "Hex": a_hex},
                      "Number of iterations": i,
                      "Number of Additions/Subtractions": addSub
                      }

    return RestoreResults

'''
    RestoreResults = {"Quotient": {"Binary": format (q, f"0{length}b"), "Hex": hex(q)},
                        "Remainder": {"Binary": format (a, f"0{length}b"), "Hex": hex(a)},
                        "Number of iterations": i,
                        "Number of Additions/Subtractions": addSub}
                        '''