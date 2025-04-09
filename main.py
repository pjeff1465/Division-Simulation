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

    # Exctract needed data from result dictionaries
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

    # Extract Divisor length from result dictionaries
    divisor_lengths = [len(result["Operand 2"]) for result in RestoreResults]

    # Create dictionaries to store grouped values by operand lengths
    restoring_add_sub_by_length = {}
    nonrestoring_add_sub_by_length = {}
    restoring_iter_by_length = {}
    nonrestoring_iter_by_length = {}

    # group by length
    for length in set(divisor_lengths):
        restoring_add_sub_by_length[length] = []
        nonrestoring_add_sub_by_length[length] = []
        restoring_iter_by_length[length] = []
        nonrestoring_iter_by_length[length] = []

    for result in RestoreResults:
        length = len(result["Operand 2"])
        if result["Number of Additions/Subtractions"] != "Error":
            restoring_add_sub_by_length[length].append(result["Number of Additions/Subtractions"])
        if result["Number of iterations"] != "Error":
            restoring_iter_by_length[length].append(result["Number of iterations"])

    for result in NonRestoreResults:
        length = len(result["Operand 2"])
        if result["Number of Additions/Subtractions"] != "Error":
            nonrestoring_add_sub_by_length[length].append(result["Number of Additions/Subtractions"])
        if result["Number of iterations"] != "Error":
            nonrestoring_iter_by_length[length].append(result["Number of iterations"])
    
    avg_lengths = sorted(set(divisor_lengths))
    avg_restoring_add_subs = [
        sum(restoring_add_sub_by_length[length]) / len(restoring_add_sub_by_length[length])
        if restoring_add_sub_by_length[length] else 0
        for length in avg_lengths
    ]
    avg_nonrestoring_add_subs = [
        sum(nonrestoring_add_sub_by_length[length]) / len(nonrestoring_add_sub_by_length[length])
        if nonrestoring_add_sub_by_length[length] else 0
        for length in avg_lengths
    ]
    avg_restoring_iter = [
        sum(restoring_iter_by_length[length]) / len(restoring_iter_by_length[length])
        if restoring_iter_by_length[length] else 0
        for length in avg_lengths
    ]
    avg_nonrestoring_iter = [
        sum(nonrestoring_iter_by_length[length]) / len(nonrestoring_iter_by_length[length])
        if nonrestoring_iter_by_length[length] else 0
        for length in avg_lengths
    ]    

    # === Figure 1: Add/Sub ===
    plt.figure(figsize=(10, 6))
    plt.plot(avg_lengths, avg_restoring_add_subs, 'b-o', linewidth=2, markersize=8, label="Restoring Method")
    plt.plot(avg_lengths, avg_nonrestoring_add_subs, 'r--s', linewidth=2, markersize=8, label="Non-Restoring Method")
    plt.title("Average Additions/Subtractions vs Divisor Length")
    plt.xlabel("Divisor Length")
    plt.ylabel("Avg. Number of Additions/Subtractions")
    plt.legend()
    plt.grid(True)
    plt.ylim(14, max(avg_restoring_add_subs + avg_nonrestoring_add_subs) + 2)  # Set y-axis range
    plt.yticks(np.arange(14, max(avg_restoring_add_subs + avg_nonrestoring_add_subs) + 2, 1))
    plt.savefig('add_sub_comparisons.png')

    # === Figure 2: Iterations ===
    plt.figure(figsize=(10, 6))
    plt.plot(avg_lengths, avg_restoring_iter, 'b-o', linewidth=2, markersize=8, label="Restoring Method")
    plt.plot(avg_lengths, avg_nonrestoring_iter, 'r--s', linewidth=2, markersize=8, label="Non-Restoring Method")
    plt.title("Average Iterations vs Divisor Length")
    plt.xlabel("Divisor Length")
    plt.ylabel("Avg. Number of Iterations")
    plt.legend()
    plt.grid(True)
    plt.ylim(8, max(avg_restoring_iter + avg_nonrestoring_iter) + 2)  # Set y-axis range
    plt.yticks(np.arange(8, max(avg_restoring_iter + avg_nonrestoring_iter) + 2, 1))
    plt.savefig('iter_comparisons.png')

    plt.show()

# can use functions PrintRestore, PrintNonRestore to print individual tables
# use PrintResults to print combined table
if __name__ == "__main__":
    NonRestoreResults, RestoreResults = main()
    #PrintRestore(RestoreResults)
    #PrintNonRestore(NonRestoreResults)
    
    graph(NonRestoreResults, RestoreResults) 

    #PrintResults(NonRestoreResults, RestoreResults)