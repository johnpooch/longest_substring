
def longest(input_string):
    longest_substring = []

    for i in range(len(input_string)):
        substring = [input_string[i]]
        for j in range(i + 1, len(input_string)):
            if input_string[j] in substring:
                break
            substring.append(input_string[j])
        if len(substring) > len(longest_substring):
            longest_substring = substring

    return len(longest_substring)
