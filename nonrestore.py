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
import sys

def NonRestoring(q, m, length):
  i = 0 #iterations
  n = length #Number of bits in q
  addSub = 0 #Number of Additions and Subtractions
  a = 0 #a = length of q

  # Check Overflow
  if(CheckOverflow(q, m, length)): # overflow has occured!
      return {
          "Quotient": {"Binary": "Error Overflow!", "Hex": "Error"},
          "Remainder": {"Binary": "Error", "Hex": "Error"},
          "Number of iterations": "Error",
          "Number of Additions/Subtractions": "Error"
      }
   
  # Check if divisor is 0 
  if m == 0:
    return {
        "Quotient": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
        "Remainder": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
        "Number of iterations": "Error",
        "Number of Additions/Subtractions": "Error"
    }   

  # Enter NonRestore Algorithm
  while i < n:
      # Preform SHL
      a, q = ShiftLeft(a, q, length)

      if BitPosition(a, length): # A is negative
          # add a <- a + m
          a = AddBinary(a, m, length)
          addSub += 1
      else: # A is positive
          # subtract a <- a - m 
          a = SubBinary(a, m, length)
          addSub += 1

      if BitPosition(a, length): # A is negative
          q = q & ~1 # clear LSB in q , q[0] = 0
      else: # A is positive
          q = q | 1 # LSB in q is 1 q[0] = 1
      
      i += 1 
        
    # On last iteration if A is negative => A <- A + M
  if BitPosition(a, length): 
        a = AddBinary(a, m, length)
        addSub += 1

      #Store everything in a dictionary
  NonRestoreResults = {"Quotient": {"Binary": format (q, f"0{length}b"), "Hex": hex(q)},
                      "Remainder": {"Binary": format (a, f"0{length}b"), "Hex": hex(a)},
                      "Number of iterations": i,
                      "Number of Additions/Subtractions": addSub}

  return NonRestoreResults
