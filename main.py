from funcs import *
from restore import Restoring
from nonrestore import NonRestoring

def test():
    print("Starting main function")
    
    q_bin = "1001"  # 9
    m_bin = "0100"  # 4

    # convert binary strings to integers
    q = int(q_bin, 2)
    m = int(m_bin, 2)
    length = len(q_bin)

    print(f"Calling Restoring with q={q}, m={m}, length={length}")
    result = Restoring(q, m, length)
    print("Received result:", result)
    
    try:
        print("\n=== Restoring Division Result ===")
        print(f"Operand 1 (Q): {q_bin} (Decimal: {q})")
        print(f"Operand 2 (M): {m_bin} (Decimal: {m})")
        print(f"Quotient:  {result['Quotient']['Binary']} (Hex: {result['Quotient']['Hex']}, Decimal: {result['Quotient']['Decimal']})")
        print(f"Remainder: {result['Remainder']['Binary']} (Hex: {result['Remainder']['Hex']}, Decimal: {result['Remainder']['Decimal']})")
        print(f"Iterations: {result['Number of Iterations']}")
        print(f"Adds/Subs:  {result['Number of Additions/Subtractions']}")
    except Exception as e:
        print(f"Error accessing result: {e}")
        print(f"Result type: {type(result)}")
        if isinstance(result, dict):
            print(f"Result keys: {result.keys()}")

def main():
    input_list = [
        {"q": "111100001", "m": "01111"},
        {"q": "001001101", "m": "11011"},
        {"q": "000010101", "m": "10011"},
        {"q": "100001101", "m": "01101"},
        {"q": "1111111000001", "m": "0000000"},
        {"q": "0010110110010", "m": "1011011"},
        {"q": "1000010111101", "m": "1000111"},
        {"q": "1100111100010", "m": "1110111"},
        {"q": "01111111000000001", "m": "011111111"},
        {"q": "10001011110110101", "m": "000110011"},
        {"q": "00011011111001000", "m": "001110111"},
        {"q": "00000101001001011", "m": "101010101"},
        {"q": "111111111100000000001", "m": "11111111111"},
        {"q": "100000111000101101100", "m": "10000111101"},
        {"q": "100011100011000111001", "m": "00101010101"},
        {"q": "000010101100000010000", "m": "00001111000"},
        {"q": "0111111111110000000000001", "m": "0111111111111"},
        {"q": "1000111000110111000111001", "m": "1010101010101"},
        {"q": "1000000111110001100011001", "m": "1000011111111"},
        {"q": "1000011100001000100100000", "m": "0000011100000"},
    ]

        #NonRestoreResults = []
    RestoreResults = []

        # Restore Function Loop
    for i, input_pair in enumerate(input_list):
        q_bin = input_pair["q"]
        m_bin = input_pair["m"]

        q_int = int(q_bin, 2)
        m_int = int(m_bin, 2)
        q_len = len(q_bin) # Track length of bin_q for leading 0's

        # Call restore function
        result = Restoring(q_int, m_int, q_len)

        # add original input (include padded binary)
        result["Operand 1"] = q_bin
        result["Operand 2"] = m_bin

        RestoreResults.append(result)
        print(result)

    print("\n=== Restoring Division Results ===")
    print("-" * 146)
    print("| {:<4} | {:<26} | {:<14} | {:<35} | {:<34} | {:<4} | {:<7} |".format(
        "No.", "Dividend", "Divisor", "Quotient (Bin/Hex)", "Remainder", "Iter", "Add/Sub"))
    print("-" * 146)
    
    for i, result in enumerate(RestoreResults):
        print("| {:<4} | {:<26} | {:<14} | {:<35} | {:<34} | {:<4} | {:<7} |".format(
            i+1,
            result["Operand 1"],
            result["Operand 2"],
            f"{result['Quotient']['Binary']} ({result['Quotient']['Hex']})",
            f"{result['Remainder']['Binary']} ({result['Remainder']['Hex']})",
            result["Number of iterations"],
            result["Number of Additions/Subtractions"]
        ))
    print("-" * 146)

    # Non Restore Function Loop
    '''
    for i in input_list:
        q_bin = i["q"]
        m_bin = i["m"]

        q_int = int(q_bin, 2)
        m_int = int(m_bin, 2)
        q_len = len(q_bin) # Track length of bin_q for leading 0's

        # Call restore function
        NonRestoreResults = NonRestoring(q_int, m_int, q_len)

        # add original input (include padded binary)
        NonRestoreResults["Operand 1"] = q_bin
        NonRestoreResults["Operand 2"] = m_bin

        NonRestoreResults.append(NonRestoreResults)
    '''

if __name__ == "__main__":
    main()

    ''' Checks for funcs.py functions
    CHECKS SHIFTLEFT FUNCTION
    q_str = "0100"
    length = len(q_str)

    q = 4
    m = 2
    a = 0

    result = ShiftLeft(a, q, length)
    print(result)

    # q = dividend
    # m = divisor 

    # Check SubBinary function
    # two binary numbers as strings
    q_bin = input("Enter the first number (binary): ")
    #b_bin = input("Enter the second number (binary): ")

    # convert binary strings to integers
    q = int(q_bin, 2)
    #m = int(m_bin, 2)

    print(f"numbers in binary: {q_bin}")

    #result = SubBinary(q, m)
    #result = AddBinary(q, m)

    #print(f"Result (integer): {result}")
    #print(f"Result (binary): {format(result, 'b')}") # binary format with 2's comp handling

    # Check bit position function
    # Check MSB of a (integer)
    length = len(q_bin)
    position = BitPosition(q, length)

    print(f"leftmost bit of {q_bin} is: {position}")
    print(length)
    '''
