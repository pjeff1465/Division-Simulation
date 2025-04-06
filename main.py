from funcs import *

if __name__ == "__main__":
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