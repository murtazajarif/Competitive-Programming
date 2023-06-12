# Define a function to compute the cycle length of an integer n
def cycle_length(n):
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        count += 1
    return count

# Prompt the user to enter the number of test cases
num_cases = int(input("Enter the number of test cases: "))

# For each test case, prompt the user to enter the range of integers i and j
for case in range(num_cases):
    i, j = map(int, input(f"Enter the range of test case #{case+1}: ").split())

    # Initialize a variable to store the maximum cycle length
    max_length = 0

    # If i is greater than j, swap the values of i and j
    if i > j:
        i, j = j, i

    # For each integer in the range [i, j], compute its cycle length
    for n in range(i, j+1):
        length = cycle_length(n)

        # Update max_length if the cycle length is greater
        if length > max_length:
            max_length = length

    # Print the output in the format "Test case #X: i j max_length"
    print(f"Test case #{case+1}: {i} {j} {max_length}")
