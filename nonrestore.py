"""
Check Overflow
  if Q >= M then there is overflow (funcs.py for overflow)
    return error
do while n >= 0 (n = number of bits in Q)
  Check Sign Bit of A (funcs.py for BitPosition(a) true = neg)
    if = 0, SHL, A=A-M (funcs.py for sub)
    if = 1, SHL, A=A+M (funcs.py for add)
  Check Sign Bit of A
    if = 0, Q[0] = 1 (funcs.py for )
    if =1, Q[1] = 0
  n--
  i++ (iteration counter int i = 0)
if sign bit of a = 1
  a = a+ m
"""
from funcs import *

# q_int, m_int ==> magnitudes (negate sign bit) ==> q_sign, m_sign
def NonRestoring(q_int, m_int, q_sign, m_sign, length):
  i_nr = 0 # iterations
  n = length # Number of bits in q
  addSub_nr = 0 # Number of Additions and Subtractions
  a = 0 # a = length of q
  q = q_int # update every iteration

  # Check Overflow
  if(CheckOverflow(q_int, m_int, length)): # overflow has occured!
      return {
          "Quotient": {"Binary": "Error Overflow!", "Hex": "Error"},
          "Remainder": {"Binary": "Error", "Hex": "Error"},
          "Number of iterations": "Error",
          "Number of Additions/Subtractions": "Error"
      }
   
  # Check if divisor is 0 
  if m_int == 0:
    return {
        "Quotient": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
        "Remainder": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
        "Number of iterations": "Error",
        "Number of Additions/Subtractions": "Error"
    }   
  # if either check true skip loop for iteration and print error

  # Enter NonRestore Algorithm
  while i_nr < n: # iteration # = num of bits
      # Preform SHL on AQ
      a, q_int = ShiftLeft(a, q, length) # use updated q

      if BitPosition(a, length): # A is negative
          # add a <- a + m
          a = AddBinary(a, m_int, length)
          addSub_nr += 1
      else: # A is positive
          # subtract a <- a - m 
          a = SubBinary(a, m_int, length)
          addSub_nr += 1

      if BitPosition(a, length): # A is negative
          q = q & ~1 # clear LSB in q , q[0] = 0
      else: # A is positive
          q = q | 1 # LSB in q is 1 q[0] = 1
      
      i_nr += 1 
        
  # On last iteration if A is negative => A <- A + M
  if BitPosition(a, length): 
    a = AddBinary(a, m_int, length)
    addSub_nr += 1
  
  # final values determined from loop
  final_q = q
  final_a = a

  # determine correct sign bit of quotient and remainder
  quotient_sign = 0 if (q_sign == m_sign) else 1
  remainder_sign = q_sign # remainder sign same as quotient

  # Take signed binary format of quotient (q) and remainder (a)
  q_bin = f"{quotient_sign}{format(abs(final_q), f'0{length - 1}b')}"
  a_bin = f"{remainder_sign}{format(abs(final_a), f'0{length - 1}b')}"

  finalq_int = binary_to_int(q_bin)
  finala_int = binary_to_int(a_bin)

  # Take signed hex format of quotient (q) and remainder (a)
  q_hex = hex(abs(finalq_int)) if finalq_int >= 0 else '-0x' + hex(abs(finalq_int))[2:]
  a_hex = hex(abs(finala_int)) if finala_int >= 0 else '-0x' + hex(abs(finala_int))[2:]

  # Store everything in a dictionary
  NonRestoreResults = {"Quotient": {"Binary": q_bin, "Hex": q_hex},
                       "Remainder": {"Binary": a_bin, "Hex": a_hex},
                       "Number of iterations": i_nr,
                       "Number of Additions/Subtractions": addSub_nr
                       }
  print(i_nr)
  
  return NonRestoreResults
