# Function to calculate the minimum number of steps from a to b
def calculate_min_steps(a, b):
    steps = 0  # Initialize the number of steps to 0
    diff = b - a  # Calculate the initial difference between a and b

    while True:  # Continue until a break statement is encountered
        if diff == 0:  # If the difference is 0, a and b are the same
            result = 2 * steps  # The result is 2 times the number of steps taken
            break
        elif diff < 2 * (steps + 1):  # If the remaining difference can be covered in 1 or 2 steps
            if steps + 1 >= diff:  # If the remaining difference can be covered in 1 step
                result = 2 * steps + 1  # The result is 2 times the number of steps plus 1
            else:  # If the remaining difference requires 2 steps
                result = 2 * steps + 2  # The result is 2 times the number of steps plus 2
            break

        steps += 1  # Increment the number of steps
        diff = b - a - steps * (1 + steps)  # Calculate the remaining difference after taking the current number of steps

    return result

# Read the number of test cases from the user
n = int(input("Enter the number of test cases: "))

# Process each test case
for _ in range(n):
    # Read a and b for each test case from the user
    a, b = map(int, input().split())

    # Calculate the minimum number of steps
    min_steps = calculate_min_steps(a, b)

    # Print the result for each test case
    print("Minimum number of steps:", min_steps)
