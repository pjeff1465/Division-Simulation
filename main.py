import matplotlib.pyplot as plt
import numpy as np
from funcs import *
from restore import Restoring
from nonrestore import NonRestoring

def test():
    print("Starting main function")
    
    q_bin = "0001"  # 1
    m_bin = "0100"  # 4

    # convert binary strings to integers
    q = int(q_bin, 2)
    m = int(m_bin, 2)
    length = len(q_bin)
    q = -32768
    m = -1
    length = 16

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

    NonRestoreResults = []
    RestoreResults = []

        # Restore Function Loop
    for i, pair in enumerate(input_list):
        q_bin = pair["q"]
        m_bin = pair["m"]

        q_sign = 1 if q_bin[0] == '1' else 0
        m_sign = 1 if m_bin[0] == '1' else 0

        q_int = int(q_bin[1:], 2) if q_sign else int(q_bin, 2)
        m_int = int(m_bin[1:], 2) if m_sign else int(m_bin, 2)

        length = len(q_bin)

        # Call restore function
        result = Restoring(q_int, m_int, q_sign, m_sign, length)

        # add original input (include padded binary)
        result["Operand 1"] = q_bin
        result["Operand 2"] = m_bin

        RestoreResults.append(result)

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
    return RestoreResults
'''
    #Non Restore Function Loop
    for i, input_pair in enumerate(input_list):
        q_bin = input_pair["q"]
        m_bin = input_pair["m"]

        q_sign = -1 if q_bin[0] == '1' else 1
        m_sign = -1 if m_bin[0] == '1' else 1

        q_int = int(q_bin[1:], 2) if q_sign == -1 else int(q_bin, 2)
        m_int = int(m_bin[1:], 2) if m_sign == -1 else int(m_bin, 2)

        length = len(q_bin)

        # Call Non Restore function
        result = NonRestoring(q_int, m_int, q_sign, m_sign, length)

        # add original input (include padded binary)
        result["Operand 1"] = q_bin
        result["Operand 2"] = m_bin

        NonRestoreResults.append(result)

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
    '''
    #return NonRestoreResults, RestoreResults


def testmain():
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

    NonRestoreResults = []
    RestoreResults = []

    for method, results_list in [("restore", RestoreResults), ("nonrestore", NonRestoreResults)]: 
        for input_pair in input_list: 
            q_bin = input_pair["q"]
            m_bin = input_pair["m"]

            q_sign = -1 if q_bin[0] == '1' else 1
            m_sign = -1 if m_bin[0] == '1' else 1

            q_int = int(q_bin[1:], 2) if q_sign == -1 else int(q_bin, 2)
            m_int = int(m_bin[1:], 2) if m_sign == -1 else int(m_bin, 2)

            length = len(q_bin)

            if method == "restore":
                result = Restoring(q_int, m_int, length)
            else:
                result = NonRestoring(q_int, m_int, length)

            result["Operand 1"] = q_bin
            result["Operand 2"] = m_bin

            results_list.append(result)

if __name__ == "__main__":
    main() 