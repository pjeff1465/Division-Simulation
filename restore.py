from funcs import *
import sys

def Restoring(q, m, length):    
    i = 0 #iterations
    n = length #Number of bits in q
    addSub = 0 #Number of Additions and Subtractions
    a = 0 # a = length of q
    
    # works here
    #print(n)
    
    # Check Overflow
    if(CheckOverflow(q, m, length)): # overflow has occured!
        return {
            "Quotient": {"Binary": "Error Overflow!", "Hex": "Error"},
            "Remainder": {"Binary": "Error", "Hex": "Error"},
            "Number of iterations": "Error",
            "Number of Additions/Subtractions": "Error"
        }

    # Check if divisor is 0
      # Check if divisor is 0 
    if m == 0:
        return {
            "Quotient": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
            "Remainder": {"Binary": "Error! Divisor = 0", "Hex": "Error"},
            "Number of iterations": "Error",
            "Number of Additions/Subtractions": "Error"
        }   
    
    # Enter Restore Algorithm
    while i < n:
        # Works here
        #print("entered while loop")

        a, q = ShiftLeft(a, q, length) # perform SHL on AQ

        a = SubBinary(a, m, length)
        addSub += 1
                
        if BitPosition(a, length): # If A = negative
            q = q & ~1 # clear LSB in q

            # restore a ( a <- a + m )
            a = AddBinary(a, m, length)
            addSub += 1 # add operation so + 1

        else: # A is positive
            q = q | 1

        i += 1 # + 1 for number of iterations

        #Store everything in a dictionary
    RestoreResults = {"Quotient": {"Binary": format (q, f"0{length}b"), "Hex": hex(q)},
                        "Remainder": {"Binary": format (a, f"0{length}b"), "Hex": hex(a)},
                        "Number of iterations": i,
                        "Number of Additions/Subtractions": addSub}

    return RestoreResults

    ''' Test Code for RESTORE 
    try:
        print("Step 1: Initializing variables")
        i = 0  # iterations
        n = length  # Number of bits in q
        addSub = 0  # Number of Additions and Subtractions
        a = 0  # a = length of q
        
        print(f"Step 2: Initial values - q={q}, m={m}, length={length}, a={a}")
        
        # Check for division by zero
        if m == 0:
            print("Error: Division by zero")
            sys.exit(1)
        
        print("Step 3: Starting the main loop")
        # Process n bits - using a for loop instead of while for clarity
        for i in range(n):
            print(f"Step 4: Iteration {i+1} beginning")
            
            print("Step 5: About to call ShiftLeft")
            try:
                a, q = ShiftLeft(a, q, length)
                print(f"Step 6: After ShiftLeft - a={a}, q={q}")
            except Exception as e:
                print(f"ERROR in ShiftLeft: {e}")
                raise
            
            print("Step 7: About to call SubBinary")
            try:
                a = SubBinary(a, m, length)
                addSub += 1
                print(f"Step 8: After SubBinary - a={a}")
            except Exception as e:
                print(f"ERROR in SubBinary: {e}")
                raise
            
            print("Step 9: About to call BitPosition")
            try:
                is_negative = BitPosition(a, length)
                print(f"Step 10: BitPosition result - is_negative={is_negative}")
            except Exception as e:
                print(f"ERROR in BitPosition: {e}")
                raise
            
            print("Step 11: Checking result of BitPosition")
            if is_negative:  # If A = negative
                print("Step 12a: A is negative, Q0=0")
                # Q0 is already 0 from shift
                
                print("Step 13a: About to restore A by calling AddBinary")
                try:
                    a = AddBinary(a, m, length)
                    addSub += 1
                    print(f"Step 14a: After restoring A - a={a}")
                except Exception as e:
                    print(f"ERROR in AddBinary: {e}")
                    raise
            else:  # A is positive
                print("Step 12b: A is positive, setting Q0=1")
                try:
                    q = q | 1  # Set LSB to 1
                    print(f"Step 13b: After setting Q0=1 - q={q}")
                except Exception as e:
                    print(f"ERROR setting Q0: {e}")
                    raise
        
        print("Step 15: Finished main loop, preparing result dictionary")
        # Prepare result dictionary
        result = {
            "Quotient": {
                "Binary": format(q, f"0{length}b"),
                "Hex": hex(q),
                "Decimal": q
            },
            "Remainder": {
                "Binary": format(a, f"0{length}b"),
                "Hex": hex(a),
                "Decimal": a
            },
            "Number of Iterations": n,
            "Number of Additions/Subtractions": addSub
        }
        
        print("Step 16: Returning result")
        return result
        
    except Exception as e:
        print(f"ERROR in Restoring function: {e}")
        print(f"Error occurred at line: {sys.exc_info()[2].tb_lineno}")
        raise
        
    '''