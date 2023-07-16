# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

# For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps. The number 32 has binary representation 100000 and has no binary gaps.

# Write a function:

# def solution(N)

# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..2,147,483,647].


def solution(N):
    # Convert N to binary representation
    binary_str = bin(N)[2:]

    # Variables to keep track of the gap length and maximum gap length
    gap_length = 0
    max_gap_length = 0

    # Flag to indicate if we are inside a gap
    in_gap = False

    # Traverse the binary representation
    for digit in binary_str:
        if digit == '1':
            # If we encounter '1', check if we were inside a gap
            # Update the maximum gap length if the current gap is longer
            if in_gap and gap_length > max_gap_length:
                max_gap_length = gap_length
            # Reset the gap_length and in_gap flag
            gap_length = 0
            in_gap = True
        elif digit == '0':
            # If we encounter '0' and are inside a gap, increment the gap_length
            if in_gap:
                gap_length += 1

    return max_gap_length

# Test cases
print(solution(1041))  # Output: 5
print(solution(32))    # Output: 0
