"""
Check Overflow
  if Q >= M then there is overflow (funcs.py for overflow)
    return error
Check XOR of Q and M (funcs.py for XOR?!)
  if 1
    return true
  if 0
    return false
do while n >= 0 (n = number of bits in Q)
  Check Sign Bit of A (funcs.py for BitPosition(a) true = neg)
    if = 0, SHL, A=A-M (funcs.py for sub)
    if = 1, SHL, A=A+M (funcs.py for add)
  Check Sign Bit of A
    if = 0, Q[0] = 1 (funcs.py for )
    if =1, Q[1] = 0
  n--
  i++ (iteration counter int i = 0)

if result != XOR of Q and M
 reult = ~result (2s complement)
"""
from funcs import *

def NonRestoring(q, m, length):
    i = 0 #iterations
    n = length #Number of bits in q
    addSub = 0 #Number of Additions and Subtractions

    #Check Overflow
    if((CheckOverflow(q, m, length)) == True): # overflow has occured!
        print(f'Overflow has occurred! Exiting program.')
        exit
    else:
      #Check XOR of Q and M

      #do while loop
      while n >= 0:
          # Perofmr SHL
          ShiftLeft(a, q, length)
          n -= 1 # -1 for SHL

          if BitPosition(a) == True: # A is negative
              # add a <- a + m
              a = AddBinary(a, m)
              addSub += 1

          else: # A is positive
              # subtract a <- a - m 
              a = SubBinary(a, m)
              addSub += 1

          if BitPosition(a) == True: # A is negative
              q[0] = 0 # Set last postion of Q to 1
          else: # A is positive
              q[0] = 1 
          
          i = i + 1 

      #Check Reult with XOR of Q and M  

    # On last iteration if A is negative => A <- A + M
    if BitPosition(a) == True: 
        a = AddBinary(a, m)
    else:
      #Store everything in a dictionary
      NonRestoreResults = [{"Quotient": {"Binary": format (q, f"0{length}b"), "Hex": hex(q)}},
                          {"Remainder": {"Binary": format (q, f"0{length}b"), "Hex": hex(a)}},
                          {"Number of iterations": i},
                          {"Number of Additions/Subtractions": addSub}]

    return NonRestoreResults
