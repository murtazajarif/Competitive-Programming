from collections import Counter

def c_p(a, b):
    count_a = Counter(a)
    count_b = Counter(b)

    common_chars = set(count_a.keys()) & set(count_b.keys())
    longest_permutation = sorted(common_chars)

    return ''.join(longest_permutation)

# Ask the user how many string pairs they want to input
num_pairs = int(input("Enter the number of string pairs: "))

# Process each string pair
for _ in range(num_pairs):
    # Read input from the user
    a = input("Enter string a: ").strip()
    b = input("Enter string b: ").strip()

    # Find the longest common permutation
    longest_permutation = c_p(a, b)

    # Print the result
    print("Longest common permutation:", longest_permutation)