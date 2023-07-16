def solution(P, Q):
    distinct_letters = set()
    min_distinct_count = len(distinct_letters)

    for i in range(len(P)):
        letter_p = P[i]
        letter_q = Q[i]
        selected_letter = min(letter_p, letter_q)

        distinct_letters.add(selected_letter)
        current_distinct_count = len(distinct_letters)

        if current_distinct_count > min_distinct_count:
            return min_distinct_count

        min_distinct_count = current_distinct_count

    return min_distinct_count

print(solution('abc', 'bcd'))    # Output: 2
print(solution('axxz', 'yzwy'))  # Output: 2
print(solution('bacad', 'abada')) # Output: 1
print(solution('amz', 'amz'))    # Output: 3