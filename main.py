import matplotlib.pyplot as plt
import numpy as np
from funcs import *
from restore import Restoring
from nonrestore import NonRestoring

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

    # Non Restore Function

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

        NonRestoreResults.append(result)

    return NonRestoreResults, RestoreResults

def graph(NonRestoreResults, RestoreResults):
    operand_lengths = [9, 5, 9, 5, 9, 5, 9, 5, 13, 7, 13, 7, 13, 7, 17, 9,
                    17, 9, 17, 9, 17, 9, 21, 11, 21, 11, 21, 11, 21, 11,
                    25, 13, 25, 13, 25, 13, 25, 13]
    combined_lengths = [operand_lengths[i] + operand_lengths[i+1] for i in range(0, len(operand_lengths), 2)]
    # This adds the operand1 + operand2, idk if we are supposed to do it that way or show operand 1 and operand 2 not repeating duh
    restoring_add_subs = [
        result["Number of Additions/Subtractions"]
        for result in RestoreResults
        if result["Number of Additions/Subtractions"] != "Error"
    ]    
    nonrestoring_add_subs = [
        result["Number of Additions/Subtractions"]
        for result in NonRestoreResults
        if result["Number of Additions/Subtractions"] != "Error" 
    ]

    restoring_iterations = [
        result["Number of iterations"] 
        for result in RestoreResults
        if result["Number of iterations"] != "Error" 
    ]
    nonrestoring_iterations = [
        result["Number of iterations"] 
        for result in NonRestoreResults
        if result["Number of iterations"] != "Error"
    ]

    #print(combined_lengths)
    #print(len(combined_lengths), len(restoring_add_subs), len(nonrestoring_add_subs), len(restoring_iterations), len(nonrestoring_iterations))

    # === Figure 1: Add/Sub ===
    plt.figure(figsize=(10, 6))
    plt.plot(combined_lengths, restoring_add_subs, label="Restoring Method", marker='o')
    plt.plot(combined_lengths, nonrestoring_add_subs, label="Non-Restoring Method", marker='x')
    plt.title("Additions/Subtractions vs Operand Length")
    plt.xlabel("Total Operand Length (len(q) + len(m))")
    plt.ylabel("Number of Additions/Subtractions")
    plt.legend()
    plt.grid(True)

    # === Figure 2: Iterations ===
    plt.figure(figsize=(10, 6))
    plt.plot(combined_lengths, restoring_iterations, label="Restoring Method", marker='o')
    plt.plot(combined_lengths, nonrestoring_iterations, label="Non-Restoring Method", marker='x')
    plt.title("Iterations vs Operand Length")
    plt.xlabel("Total Operand Length (len(q) + len(m))")
    plt.ylabel("Number of Iterations")
    plt.legend()
    plt.grid(True)

    plt.show()

# can use functions PrintRestore, PrintNonRestore to print individual tables
# use PrintResults to print combined table
if __name__ == "__main__":
    NonRestoreResults, RestoreResults = main()
    #PrintRestore(RestoreResults)
    #PrintNonRestore(NonRestoreResults)
    
    #graph(NonRestoreResults, RestoreResults) 

    PrintResults(NonRestoreResults, RestoreResults)