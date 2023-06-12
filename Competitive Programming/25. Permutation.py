# function to find longest string x that satisfies the given criteria
def longest_permutation_subsequence(a, b):
    # create empty dictionaries to store character counts
    a_counts = {}
    b_counts = {}

    # iterate through string a and update its character counts
    for c in a:
        if c in a_counts:
            a_counts[c] += 1
        else:
            a_counts[c] = 1

    # iterate through string b and update its character counts
    for c in b:
        if c in b_counts:
            b_counts[c] += 1
        else:
            b_counts[c] = 1

    # create an empty dictionary to store common character counts
    common_counts = {}

    # iterate through the character counts in string a
    for c in a_counts:
        # check if the character is also present in string b
        if c in b_counts:
            # add the minimum count of the character in both strings to common_counts
            common_counts[c] = min(a_counts[c], b_counts[c])

    # create an empty list to store the common characters
    common_chars = []

    # iterate through the common character counts
    for c in common_counts:
        # add the character repeated common_counts[c] times to common_chars
        common_chars.extend([c] * common_counts[c])

    # sort the common characters alphabetically and create the string
    x = ''.join(sorted(common_chars))

    return x


# read input from user at runtime
while True:
    try:
        # read two strings from user input
        a = input().strip()
        b = input().strip()

        # find the longest permutation subsequence and print it
        x = longest_permutation_subsequence(a, b)
        print(x)

    except EOFError:
        # exit if end of file is reached
        break
