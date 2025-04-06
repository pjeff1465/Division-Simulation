from funcs import *

if __name__ == "__main__":
    # Check SubBinary function
    # two binary numbers as strings
    a_bin = input("Enter the first number (binary): ")
    b_bin = input("Enter the second number (binary): ")

    # convert binary strings to integers
    a = int(a_bin, 2)
    b = int(b_bin, 2)

    print(f"numbers in binary: {a_bin}, {b_bin}")

    result = SubBinary(a, b)

    print(f"Result (integer): {result}")
    print(f"Result (binary): {format(result, 'b')}") # binary format with 2's comp handling

    # Check bit position function
    index = int(input(f"Enter index for bit position of {a_bin}: "))
    position = BitPosition(a, index)

    print(f"Bit of {a_bin} with index {index} is: {'1' if result else '0'}")