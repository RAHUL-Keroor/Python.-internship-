def min_steps_to_magic_string(s):
    # Count the frequency of each character in the string
    char_frequency = {}
    for char in s:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    # Find the maximum frequency
    max_frequency = max(char_frequency.values())

    # Calculate the minimum number of steps required
    min_steps = len(s) - max_frequency

    return min_steps

